# -*- coding: utf-8 -*-

try:
	import tkinter as tk
	from tkinter import ttk

except Exception as e:
	raise e

# Class de liaison entre les différents Menus

class Menus:


	def __init__(self):

		self.side_menu = Side_Menu()


	def __str__(self):

		return "Menus class"


class Side_Menu:


	def create_widget(self, images_path, text_controller):

		# Création du conteneur du menu 
	 	self.frame = ttk.Frame()

	 	# affichage des icons
	 	# self.video_btn = ttk.Button(self.frame, image=tk.BitmapImage(images_path  + "video.png"))
	 	self.video_btn = ttk.Button(self.frame, text=text_controller.get_text("video"))
	 	self.video_btn.grid(row=0, column=0)
	 	# self.graph_btn = ttk.Button(self.frame, image=tk.BitmapImage(images_path  + "graphs.png"))
	 	
	 	self.graph_btn = ttk.Button(self.frame, text=text_controller.get_text("graphs"))
	 	self.graph_btn.grid(row=1, column=0)
	 	# self.gps_btn = ttk.Button(self.frame, image=tk.BitmapImage(images_path  + "gps.png"))
	 	 
	 	self.gps_btn = ttk.Button(self.frame, text=text_controller.get_text("gps"))
	 	self.gps_btn.grid(row=2, column=0)

	 	return self.frame

