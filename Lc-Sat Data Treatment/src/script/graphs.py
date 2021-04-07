# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier graphs.py")
	import matplotlib.pyplot as plt
	import numpy as np

except Exception as e:
	raise e

# possibilité de customisation des graphiques:
# 	- couleur
# 	- style de courbe
# 	- nom des élements
# 	- épaisseur de la courbe
# 	- marquer les points
# 	possibilité de voir la grille


# class controller des types de garphs

class Graph:


	# Liaison entre l'interface et le graph temps
	def draw_time_graph(self, values, frequency):

		return Time_Graph(values, frequency)




# en fonction du temps

class Time_Graph:

	def __init__(self, values, frequency):

		self.values = values
		self.frequency = frequency
		self.X_values = np.array(self.create_x_values())

	# détermine l'intervalle de temps entre chaque données avec la fréquence d'enregistrement des données
	def create_x_values(self):
 
		time = 0
		self.x_values = []
		
		for i in self.values:
			self.x_values.append(time)
			time += 1 / self.frequency

		return self.x_values


	def draw_graph(self):
		
		plt.plot(self.X_values, self.values, 'r-')
		plt.show()




# class Time_Graph:

# 	def __init__(self, y_values, y_label, color, width, style, marker, grid):

# 		self.y_values = y_values
# 		self.y_label = y_label

# 		# styles
# 		self.color = color
# 		self.width = width
# 		self.style = style
# 		self.marker = marker
# 		self.grid = grid


# 	# definition des labels
# 	def define_labels(self):

# 		self.x_label =  "temps (en s)"
# 		self.title = f"{self.y_label} en fonction du {self.x_label}."


# 	# definition des coordonnées (enregistrement des données toutes les 0.1 secondes)
# 	def create_coordinates(self):
# 		time = 0
# 		self.x_values = []

# 		for i in self.y_values:

# 			self.x_values.append(time)
# 			time += 0.1

# 		self.X_values = np.array(self.x_values)
# 		self.Y_values = np.array(self.y_values)


# 	# formatage des styles choisis par l'utilisateur
# 	def create_styles(self):
# 		self.color_and_styles = "self.color"


# 	# créer et renvoit le graphique à l'application
# 	def create_graph(self):

# 		plt.title(self.title)
# 		plt.plot(self.X_values, self.Y_values)
# 		plt.xlabel(self.x_label)
# 		plt.ylabel(self.y_label)
# 		plt.legend()
# 		plt.show()


print("Fin Chargement fichier graphs.py")