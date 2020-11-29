from docx2pdf import convert


def convert_docx_to_pdf(filename_docx: str):
    rindex_dot = filename_docx.rfind('.')
    filename_pdf = filename_docx[:rindex_dot+1] + 'pdf'
    convert(filename_docx, filename_pdf)

    return filename_pdf
