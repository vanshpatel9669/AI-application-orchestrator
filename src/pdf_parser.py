import fitz


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract text from an uploaded PDF file using PyMuPDF.
    """
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    pages = []
    for page in doc:
        pages.append(page.get_text())

    return "\n".join(pages).strip()