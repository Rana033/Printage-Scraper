import qrcode
import io
from reportlab.lib.utils import ImageReader


def generate_qr_code(text):
    qr = qrcode.QRCode(version = 1,
                box_size = 5,
                border = 3,
                )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image()
    buffer = io.BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return ImageReader(buffer)
