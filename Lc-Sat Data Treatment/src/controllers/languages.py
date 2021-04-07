# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier languages.py")
	import json
except Exception as e:
	raise e

# Communique les texts en fonction de la langue

class Language:

	def __init__(self, file_path):

		self.file_path = file_path

		with open(self.file_path, 'r') as f:
			self.data = json.load(f)
			f.close()


	def __str__(self):

		return "Conts Controller"


	def get_text(self, text):
		
		return self.data[text]

print("Fin Chargement fichier languages.py")