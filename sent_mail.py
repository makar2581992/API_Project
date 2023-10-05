import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


fromaddr = 'mail@mail.ru'
pswd = 'gi89mjb90f'
reportname = 'log.txt'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['Subject'] = 'отчет от питона'
text = 'отчет от питона log.txt'

msg.attach(MIMEText(text))

with open(reportname, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="{basename(reportname)}"'
    msg.attach(part)


server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, pswd)
text = msg.as_string()
server.sendmail(fromaddr, text)
server.quit()