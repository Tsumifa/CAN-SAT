# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier Themes.py")
	import json

except Exception as e:
	raise e

# Communique les styles en fonction du thème

class Theme:

	def __init__(self, file_path):

		self.file_path = file_path

		with open(self.file_path, 'r') as f:
			self.data = json.load(f)
			f.close()


	def __str__(self):

		return "Conts Controller"


	def get_theme(self, theme_content):
		
		return self.data[theme_content]


print("Fin Chargement fichier Themes.py")