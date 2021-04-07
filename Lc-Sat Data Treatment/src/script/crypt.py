# -*- coding: utf-8 -*-

try:
	print("Chargement fichier crypt.py")
	import pyAesCrypt
	import shutil
	import zipfile
	import os

except Exception as e:
	raise e


# décompresse le fichier + décrypt les fichiers du dossier

class Decrypt:


	def __str__(self):

		return "Decrypt class"


	# Décrypt le fichier
	def decrypt(self, folder_path, destination, data_type, password):

		print("chemin fichier :{0}\nchemin destination: {1}\ntype_donnée: {2}\nmdp: {3}".format(folder_path, destination, data_type, password))

		# filename, file_extension = os.path.splitext(folder_path)
		# # Décompresse le fichier
		# if file_extension == '.gz':
			
		# 	shutil.unpack_archive(folder_path, destination)

		# # Transfert les fichiers si le dossier est déjà décompressé
		# else:

		# 	for filename in os.listdir(folder_path):
		# 		shutil.copyfile(filename, destination)

		#  # Décrypte chaque fichier:
		#  # 	- key est le nom initial
		#  # 	- value est le nom final
		# for key, value in data_type.items():

		# 	pyAesCrypt.decryptFile(key, value, password, 16 * 1024)


print("Fin Chargement fichier crypt.py")