# Multi-User-Text-Extraction-Service
1. Develop a text extraction service using FastAPI, Django, or Flask, Python's modern web frameworks. 2. Ensure the service can extract text from PDF, DOC, and DOCX files.

# clone app from GIT 
`git clone https://github.com/steffyjk/Multi-User-Text-Extraction-Service.git`

# Create the env

### create environment command for window system is as below:

`python -m venv env_name`

### activate the env:

`.\env_name\Scripts\activate`

# Install the requirements

`pip install -r .\requirements.txt`

# SET up the env secrets in .env file as per .env-example file

create .env in root level add this Note: this is testing secret Key provided in env-example file.

`EMAIL_BACKEND=`

`EMAIL_HOST=`

`EMAIL_PORT=`

`EMAIL_USE_TLS=True`

`EMAIL_HOST_USER=`

`EMAIL_HOST_PASSWORD=`



# run python django app:

`python .\manage.py runserver `

# Endpoints:

##### 1. POST http://127.0.0.1:8000/api/extract-and-store/:

CURL for the above enddpint is as below

`curl --location 'http://127.0.0.1:8000/api/extract-and-store/' \
--form 'email="email@gmail.com"' \
--form 'url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"'`

Expected_response: 

`{
    "message": "Document processed and stored successfully.",
    "document_id": 8,
    "extracted_text": "Dumm y PDF file"
}`




