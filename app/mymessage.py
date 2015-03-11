import smtplib

def send_mail(fromaddr,fromname,toaddr,msg,subject):
	message = """From: {} <{}>

	To: {} <{}>

	Subject: {}

	{}	

	"""

	messagetosend = message.format(

 	fromname,

 	fromaddr,

 	toname,

 	toaddr,

 	subject,

 	msg)

# Credentials (if needed)

	username = 'hevongordon@gmail.com'

	password = 'clubzzdamion98'

# The actual mail send

	server = smtplib.SMTP('smtp.gmail.com:587')

	server.starttls()

	server.login(username,password)

	server.sendmail(fromaddr, toaddr, messagetosend)

	server.quit()