from email.message import EmailMessage
import smtplib
from datetime import datetime


lcFecha = datetime.now().strftime('%Y-%m-%d') 
lcNombreArchivo = "/var/www/html/Fecha"+lcFecha+".csv"
lcNombreSolo = "Fecha"+lcFecha+".csv"

remitente = "juan.jose.agudelo@correounivalle.edu.co"
destinatario = "juan.jose.agudelo@correounivalle.edu.co"

mensaje = "Felicitaciones, si puede leer esto quiere decir que funcionó"

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Datos archivo: " + lcNombreSolo
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "dfcp eyho pjrk ckiv")

with open(lcNombreArchivo, "rb") as f:
 email.add_attachment(
  f.read(),
  filename=lcNombreSolo,
  maintype="application",
  subtype="csv"
 )



smtp.sendmail(remitente, destinatario, email.as_string())