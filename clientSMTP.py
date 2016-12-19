#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "alarma@zweicom.com"
toaddr = "receptor_mail@zweicom.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Alarma Umbral Mensajes Erroneos"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login(fromaddr, "YOUR PASSWORD")
#server = smtplib.SMTP('IP', PORT)
server = smtplib.SMTP('127.0.0.1')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
