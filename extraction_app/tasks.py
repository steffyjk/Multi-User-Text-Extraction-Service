from celery import shared_task
from PyPDF2 import PdfReader
from docx import Document as DocxDocument
from .models import DocumentDetails
from .utils import send_notification  
import os
import requests


@shared_task
def process_document(file_path, url, email):
    try:
        # Determine file type and extract text
        if file_path.endswith('.pdf'):
            reader = PdfReader(file_path)
            extracted_text = ''.join(page.extract_text() for page in reader.pages)
        elif file_path.endswith('.docx'):
            doc = DocxDocument(file_path)
            extracted_text = '\n'.join([p.text for p in doc.paragraphs])
        else:
            raise ValueError("Unsupported file format")

        # Store in database
        document = DocumentDetails.objects.create(
            file=file_path if file_path else None,
            url=url if url else None,
            extracted_text=extracted_text,
            email=email,
            status="COMPLETED",
        )

        # Send notification email
        send_notification(email, {
            "message": "Document processed and stored successfully.",
            "document_id": document.id,
            "extracted_text": extracted_text,
        })

        # Cleanup temporary file
        os.remove(file_path)

        return f"Document {document.id} processed successfully."

    except Exception as e:
        return f"Failed to process document: {str(e)}"