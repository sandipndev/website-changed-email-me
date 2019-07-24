from __future__ import print_function
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

import auth
def get_labels():
	results = service.users().labels().list(userId='me').execute()
	labels = results.get('labels', [])

	if not labels:
		print('No labels found.')
	else:
		print('Labels:')
		for label in labels:
			print(label['name'])

config_data = json.load(open("email_config.json", "r"))
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = config_data['client_id_filename']
APPLICATION_NAME = config_data['application_name']
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

import send_email

class Mail:
	def __init__(self):
		self.sendInst = send_email.send_email(service)
	def create_msg(self, to, sub, body):
		self.message = self.sendInst.create_message(config_data['email_id'], to, sub, body)
	def create_msg_attachment(self, to, sub, body, *attachments):
		self.message = self.sendInst.create_message_with_attachment(config_data['email_id'], to, sub, body, *attachments)
	def send_msg(self):
		return self.sendInst.send_message('me', self.message)
