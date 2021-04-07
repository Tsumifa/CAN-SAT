# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier Settings.py")
	import json

except Exception as e:
	raise e

# Communique les paramètres de l'application + change les paramètres

class Settings:

	def __init__(self, file_path):

		self.file_path = file_path

		with open(self.file_path, 'r') as f:
			self.data = json.load(f)
			f.close()


	def __str__(self):

		return "Settings Controller"


	def get_setting(self, setting_name):
		
		return self.data[setting_name]

	
	def update_setting(self, setting_name, new_value):
		
		self.data[setting_name] = new_value

		with open(self.file_path, 'w') as f:
			json.dump(self.data, f, indent=4)
			f.close()

print("Fin Chargement fichier Settings.py")