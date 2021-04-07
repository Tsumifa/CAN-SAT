# -*- coding: utf-8 -*-

try:
	print("Chargement fichier read_data.py")
	import pickle
	import numpy as np

except Exception as e:
	raise e

# lit et enregistre les données des fichiers décryptés dans des arrays numpy


class Data_Reader:

	def __init__(self, folder_path):

		self.folder_path = folder_path


	def __str__(self):

		return "Data Reader"


	def read_data(self):

		data = pickle.load(open(self.folder_path + "data.bin", "rb"))

		self.pression = np.array(data["press"], dtype="float64")
		self.temperature = np.array(data["temp"], dtype="float64")
		self.altitude = np.array(data["alt"], dtype="float64")
		self.x_acceleration = np.array(data["ax"], dtype="float64")
		self.y_acceleration = np.array(data["ay"], dtype="float64")
		self.z_acceleration = np.array(data["az"], dtype="float64")
		self.latitude = np.array(data["lat"], dtype="float64")
		self.longitude = np.array(data["lon"], dtype="float64")
		self.satellite = np.array(data["sat"], dtype="float64")
		self.quality = np.array(data["qual"], dtype="float64")
		self.speed = np.array(data["speed"], dtype="float64")
		self.thermique = np.array(data["therm"], dtype="float64")
		# self.humidity = np.array(data["hum"])
		print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t".format(self.pression, self.temperature, self.altitude, self.x_acceleration, self.y_acceleration, self.z_acceleration, self.latitude, self.longitude, self.satellite, self.quality, self.speed, self.thermique))

print("Fin Chargement fichier read_data.py")