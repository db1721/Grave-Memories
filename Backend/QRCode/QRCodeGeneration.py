from qrcodegen import *

#Code is just for refernce
# Simple operation
qr0 = QrCode.encode_text("Hello, world!", QrCode.Ecc.MEDIUM)
svg = QrCode.to_svg_str(qr0, 4)  # See qrcodegen-demo


# Manual operation
segs = QrSegment.make_segments("3141592653589793238462643383")
qr1 = QrCode.encode_segments(segs, QrCode.Ecc.HIGH, 5, 5, 2, False)
for y in range(qr1.get_size()):
    for x in range(qr1.get_size()):
        print("hi")
        # (... paint qr1.get_module(x, y) ...)
