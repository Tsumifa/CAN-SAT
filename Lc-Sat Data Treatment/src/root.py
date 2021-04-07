# -*- coding: utf-8 -*-

try:
	print("Chargement Root.py")
	import tkinter as tk

except Exception as e:
	raise e


# Class de gestion de l'interface

class Root:


	def __init__(self, controllers, models, views, scripts):
		
		self.controllers = controllers
		self.models = models
		self.views = views
		self.scripts = scripts

		self.app()


	def __str__(self):
		return "Root class"


	def app(self):

		self.root = tk.Tk()
		self.configure_window()
		self.open_load_data_window()
		self.root.mainloop()


	# applique les configurations
	def configure_window(self):
		
		self.root.title(self.controllers.language_controller.get_text("title"))
		self.root.geometry(self.controllers.consts_controller.get_consts("WIN_SIZE"))
		self.root.iconbitmap(self.controllers.path_controller.get_path("IMG_PATH") + "logo.ico")
		self.root.configure(bg=self.controllers.theme_controller.get_theme("backgroundColor"))


	# retire l'ensemble des widgets présents dans la frame séclectionnée
	def clear_window(self, frame):
		
		frame.destroy()


	# Lance le décryptage des fichiers sélectionnés
	def decrypt(self, path, key):
		
		data_type = {}
		for filename in self.controllers.setting_controller.get_setting("data_type"):
			data_type[self.controllers.path_controller.get_path("FILES_DATA") + "data/" + filename + ".aes"] = self.controllers.path_controller.get_path("FILES_DATA") + filename 

		self.scripts.decrypt.decrypt(
			path,
			self.controllers.path_controller.get_path("FILES_DATA"),
			data_type,
			key
			)


	# Destruction des composants de la fenêtre load_data
	# Décryptage des données
	# Appel de la page principale
	def close_load_data_window(self):
		
		key = self.views.load_data.key_input.get()
		path = self.views.load_data.path_label["text"]

		if key != '' and path != '':
			self.clear_window(self.frame_container)
			self.decrypt(path, key)
			self.open_main_window()

		else:
			print("error")


	def open_load_data_window(self):

		self.frame_container = tk.Frame()
		self.frame_container.pack()

		self.views.load_data.create_widget(self.frame_container)

		# boutton pour lancer le décryptage des données
		self.confirm_button = self.models.buttons.valid_button.create_widget(self.frame_container, self.controllers.language_controller.get_text("decrypt"))
		self.confirm_button.configure(command=self.close_load_data_window)
		self.confirm_button.pack()
		

	# Affiche les composants graphiques de la page principale
	def open_main_window(self):

		self.views.main_view.create_widget()

print("Fin Chargement fichier Root.py")