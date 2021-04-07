# -*- coding: utf-8 -*-

try:
	print("Chargement fichier main_view.py")
	import tkinter as tk
	from tkinter import ttk

except Exception as e:
	raise e

# Page d'import et de décryptage des données
 
class Main_Window:


	def __init__(self, controllers, models, scripts):
		
		self.controllers = controllers
		self.models = models
		self.scripts = scripts


	def __str__(self):

		return "Load Data Window class"


	def render_planishpere_map(self):

		self.scripts.maps.planisphere_map.render_map(self.latitude, self.longitude)


	def render_shematic_map(self):

		self.scripts.maps.schematic_map.render_map(self.latitude, self.longitude)

	
	def render_terrain_map(self):

		self.scripts.maps.terrain_map.render_map(self.latitude, self.longitude)


	def show_map_tab(self):

		self.latitude = self.scripts.read_data.latitude
		self.longitude = self.scripts.read_data.longitude

		# affiche les différents bouttons
		self.map_frame = ttk.Frame()
		self.map_frame.grid(row=0, column=1)

		self.planisphere_button = self.models.buttons.normal_button.create_widget(self.map_frame, self.controllers.language_controller.get_text("planisphere"))
		self.planisphere_button.configure(command=self.render_planishpere_map)
		self.planisphere_button.grid(row=0, column=0)

		self.schematic_button = self.models.buttons.normal_button.create_widget(self.map_frame, self.controllers.language_controller.get_text("schematic"))
		self.schematic_button.configure(command=self.render_shematic_map)
		self.schematic_button.grid(row=0, column=1)
		
		self.terrain_button = self.models.buttons.normal_button.create_widget(self.map_frame, self.controllers.language_controller.get_text("satellite"))
		self.terrain_button.configure(command=self.render_terrain_map)
		self.terrain_button.grid(row=0, column=2)


	def create_side_menu(self):

		self.side_menu = self.models.menus.side_menu.create_widget(self.controllers.BASE_DIR + self.controllers.path_controller.get_path("IMG_PATH"), self.controllers.language_controller)
		
		self.models.menus.side_menu.video_btn.configure()
		self.models.menus.side_menu.graph_btn.configure()
		self.models.menus.side_menu.gps_btn.configure(command=self.show_map_tab)

		self.side_menu.grid(row=0, column=0)


	def create_widget(self):
		
		self.scripts.read_data.read_data()
		self.create_side_menu()



print("Fin Chargement fichier main_view.py")