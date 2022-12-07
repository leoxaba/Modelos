import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# S M T P - Simple mail transfer protocol
# Para cria o servidor e enviar email

#1- Startar o servidor SMTP

host = 'smtp.furg.br'
port = '587'
login = 'leonardo.schabbach@furg.br'
senha = '*****'

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login,senha)

#2- Construir o email tipo MIME

corpo = "olah Mundo!"

# Montando o Email
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = 'arquivorh@furg.br'
email_msg['Subject'] = "E-mail automático do Léo"
email_msg.attach(MIMEText(corpo, 'plain'))



#3- Enviar o email tipo MIME no servidor SMTP

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()