import os
import smtplib
import imghdr
from email.message import EmailMessage

# This is required to allow access for python
# Go to this site and turn less secure on if two factor is off
# https://myaccount.google.com/lesssecureapps
# Or go to this site if two factor is on and create the app password to log in the email
# https://myaccount.google.com/apppasswords

# Use environment variables for security
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


# List of contacts to send email to
contacts = [EMAIL_ADDRESS]

# message construction
msg = EmailMessage()
msg['Subject'] = 'Email List'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
# OR
# msg['To'] = EMAIL_ADDRESS


# Text Content
msg.set_content('Reading Material')


# Image Email Attachment
files_img = ['Model_1.png', 'IMG_8810.jpg']
for file in files_img:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)


# Pdf Attachment
files = ['home.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


# HTML Email Attachment
# msg.add_alternative('''\
# <!DOCTYPE html>
# <html lang="en">
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email.</h1>
#     </body>
# </html>
# ''', subtype='html'
#                     )


# Login and Sending
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
