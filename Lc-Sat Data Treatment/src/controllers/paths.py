# -*- coding: utf-8 -*-

try:
	print("Chargement fichier paths.py")
	import json

except Exception as e:
	raise e


# Communique les chemins relatifs des fichiers

class Paths:

	def __init__(self, file_path, base_path):
		
		self.file_path = file_path
		self.base_path = base_path

		with open(self.file_path, 'r') as f:
			self.data = json.load(f)
			f.close


	def __str__(self):

		return 'Path Controller'


	def get_path(self, file_name):

		return self.base_path + self.data[file_name]


print("Fin Chargement fichier paths.py")