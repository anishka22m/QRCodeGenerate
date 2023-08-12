#import the necessary module!
import pyqrcode

# Define the data

data = input("Enter your link: ")

# Create qrcode:
qr = pyqrcode.create(data)

# Save the qrcode in png format with proper scaling:
qr.png("YourQRCode.png", scale= 5)
print("QR code saved")
     