# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier loadContst.py")
	import json

except Exception as e:
	raise e

# Communique les constantes de l'application

class Load_Consts:

	def __init__(self, file_path):

		self.file_path = file_path

		with open(self.file_path, 'r') as f:
			self.data = json.load(f)
			f.close()


	def __str__(self):

		return "Conts Controller"


	def get_consts(self, conts_name):
		
		return self.data[conts_name]

print("Fin Chargement fichier loadContst.py")