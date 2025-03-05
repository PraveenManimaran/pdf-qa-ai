import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file object."""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text