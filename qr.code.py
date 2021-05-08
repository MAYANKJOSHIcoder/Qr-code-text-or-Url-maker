import qrcode #pip install qrcode
import image #pip install image
qr = qrcode.QRCode(
    version= 15,
    box_size=10,
    border= 5
)

data = "Hi I am Mayank Joshi who made this code https://github.com/MAYANKJOSHIcoder/Qr-code-text-or-Url-maker" # write text inside this box

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = 'white')
img.save('test.png')
