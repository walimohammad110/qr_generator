import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    border=4,
    box_size=10
)

qr.add_data("https://www.youtube.com/watch?v=Z90Ieb8Oj1c")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("ww.png")
img.show()   # 👈 this opens the image