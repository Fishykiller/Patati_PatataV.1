import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'patatipatatabad@gmail.com'
msg['To'] = 'patatipatatabad@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('patatipatatabad@gmail.com', 'F011006f')
mailserver.sendmail('patatipatatabad@gmail.com', 'patatipatatabad@gmail.com', msg.as_string())
mailserver.quit()
