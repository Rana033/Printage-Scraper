from qr import*
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_for_books(books, pdf_filename):
    pdf = canvas.Canvas(pdf_filename)

    for book in books:
        title = book['title']
        url = book['link']

        # Create QR code image for each book
        qrcode_buffer =generate_qr_code(url)

        # Draw QR code on PDF
        x_position = (letter[0]-200 ) / 2  # Centering the QR code horizontally
        y_position = (letter[1]-200 ) / 2  # Centering the QR code vertically

        pdf.drawImage(qrcode_buffer, x=x_position, y=y_position,width=200,height=200)

        # Draw text under QR code
        pdf.setFont("Helvetica-Bold", 12)
        text_width = pdf.stringWidth(title, "Helvetica-Bold", 12)
        x_text_position = (letter[0] - text_width) / 2
        y_text_position = y_position -30 # Adjust as needed
        pdf.drawString(x_text_position, y_text_position , title)
        
        # Add a new page for the next book
        pdf.showPage()
        
        
        

    # Save PDF
    pdf.save()