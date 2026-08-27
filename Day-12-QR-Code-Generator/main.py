"""
DAY 12/75
PYTHON PROJECT JOURNEY
"""

import qrcode

text = input("Enter text or URL: ")

qr = qrcode.QRCode(
    box_size=1,
    border=1
)

qr.add_data(text)
qr.make(fit=True)

print("\n📱 YOUR QR CODE\n")
qr.print_ascii(invert=True)

print("\n✅ QR Code Generated!")
