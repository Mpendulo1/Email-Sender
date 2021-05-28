import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'mpendulokhozamk2@gmail.com'
receiver_email_id = 'mndabeni6@gmail.com', 'me@tsotetsithapelo.co.za'
password = input('Enter sender"s email password')
s.starttls()
s.login(sender_email_id, password)
message = 'Hello, I am testing the smtp email sender. No reply requested.'
message = message + 'Testing Testing'
s.sendmail(sender_email_id, receiver_email_id, message)
s.quit()
