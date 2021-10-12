from sys import argv
import smtplib, ssl
import config

def send(receiver, subject, content):
	ssl_context = ssl.create_default_context()
	service = smtplib.SMTP_SSL(config.smtp_server_domain_name, config.port, context=ssl_context)
	service.login(config.sender_mail, config.password)

	result = service.sendmail(config.sender_mail, receiver, f"Subject: {subject}\n{content}")
	service.quit()


if __name__ == '__main__':
	receiver = argv[1]
	subject = argv[2]
	content = argv[3]
	send(receiver, subject, content)
