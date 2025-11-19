# ATS Resume Checker

**ATS Resume Checker** is a web-based application that analyzes resumes against job descriptions using AI. It simulates an Applicant Tracking System (ATS) to give match scores, highlight missing skills, check experience mismatches, and provide overall comments.

## Features
- Upload PDF resumes and get detailed analysis.
- Match Score (0-100) based on job description.
- Detect missing skills.
- Check experience mismatches.
- Provide overall comments for improvement.
- Simple web interface built with FastAPI and Jinja2 templates.

## Tech Stack
- Backend: FastAPI
- Frontend: Jinja2 Templates
- AI: OpenRouter API (GPT-4o-mini)
- PDF Parsing: PyPDF2
- Environment: Python `venv`, `.env` for API keys
- Version Control: Git & GitHub

## Installation
1. Clone the repo:  
   git clone https://github.com/sowmiyasoundar/ATS_RESUME_CHECKER.git
   cd ATS_RESUME_CHECKER
   
2. Create a virtual environment and activate it:
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt
  
4. Create a .env file in the project root and add your OpenRouter API key:
   OPENROUTER_API_KEY=your_api_key_here
  
5. Run the server:
   uvicorn main:app --reload
  
6. Open your browser and go to:
   http://127.0.0.1:8000

## Usage:

1. Upload a PDF resume.

2. Paste the job description.

3. Click Analyze to get the results including:

             # Match Score
          
             # Missing Skills
          
             # Experience Mismatch
          
             # Overall Comment

   
## License
MIT License


## Author
Sowmiya Soundar
GitHub: https://github.com/sowmiyasoundar
