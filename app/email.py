from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail

# how does threading work in python
# why does outlook keep appending my Tim S name to my emails, even though
# i'm using yarmitporys@outlook.com

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)


def send_email(to, subject, template, **kwargs):
	app = current_app._get_current_object()
	msg = Message(app.config['NEWTAB_MAIL_SUBJECT_PREFIX'] + " " + subject,
				  sender=app.config['NEWTAB_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr

# def send_email(to, subject, template, **kwargs):
# 	app = current_app.get_current_object()
# 	msg = Message(app.config['NEWTAB_MAIL_SUBJECT_PREFIX'] + " " + subject,
# 				  sender=app.config['NEWTAB_MAIL_SENDER'], recipients=[to])
# 	msg.body = render_template(template + '.txt', **kwargs)
# 	msg.html = render_template(template + '.html', **kwargs)
# 	thr = Thread(target=send_async_email, args=[app, msg])
# 	thr.start()
# 	return thr