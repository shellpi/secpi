import settings

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib


# FUNCTION TO SEND A SECPI EMAIL #
def send_secpi_email(image, img_name: str) -> None:
	msg = MIMEMultipart()
	msg['Subject'] = settings.EMAILSUBJECT
	msg['From'] = settings.EMAILSENDERUSR
	msg['To'] = settings.EMAILRECEIVER

	text = MIMEText(settings.EMAILTEXT)
	msg.attach(text)
	image = MIMEImage(image, name=img_name)
	msg.attach(image)

	s = smtplib.SMTP(settings.EMAILSERVERHOST, settings.EMAILSERVERPORT)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(settings.EMAILSENDERUSR, settings.EMAILSENDERPSW)
	s.sendmail(From, To, msg.as_string())
	s.quit()
