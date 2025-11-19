from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
import requests
import PyPDF2

# Load API Key
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"
    return text

@app.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    job_description: str = Form(...),
    resume_file: UploadFile = File(...)
):
    # Save uploaded PDF
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)

    file_path = os.path.join(uploads_dir, resume_file.filename)
    with open(file_path, "wb") as f:
        f.write(await resume_file.read())

    # Extract text
    resume_text = extract_text_from_pdf(file_path)

    # Prepare prompt
    prompt = f"""
You are an ATS Resume Analyzer AI.

Compare the following RESUME with JOB DESCRIPTION.

Resume:
{resume_text}

Job Description:
{job_description}

Give output in this exact format:

1. **Match Score (0-100)**  
2. **Missing Skills**  
3. **Experience Mismatch**  
4. **Overall Comment**
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        ai_output = data.get("choices", [{}])[0].get("message", {}).get("content", "No output from AI.")
    except Exception as e:
        ai_output = f"Error: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": ai_output
    })
@app.get("/healthz")
def health_check():
    return {"status": "ok"}