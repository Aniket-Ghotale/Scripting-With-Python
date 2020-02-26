import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Aniket Ghotale"
email['to'] = "aniketghotale@gmail.com"
email['subect'] = "I won 1,00,000Rs."

email.set_content("I am python developer!")

with smtplib.SMTP(host="smtp.gmail.com", port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("aniketghotale2014@gmail.com", "andi992212543213")
    smtp.send_message(email)
    print("All good and successfully sending this mail...")