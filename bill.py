import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=6
)

data = "https://precious-profiterole-86190f.netlify.app"
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
image.save("new2.png")
print("QR code has been generated successfully!")

import cv2
import webbrowser
camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cv2.destroyWindow(window_name)
webbrowser.open(data)
