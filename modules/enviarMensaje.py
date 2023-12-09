# archivo: envio_correos.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar(destinatario, asunto, cuerpo):
    msg = MIMEMultipart()
    msg['From'] = 'tu_correo@gmail.com'
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'tu_contraseña')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()