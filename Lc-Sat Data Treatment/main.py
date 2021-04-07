# -*- coding: utf-8 -*-

try:
	print("Démarrage")
	# modules
	import os

	# interface
	
	from src import root
	
	# 	- controllers
	from src.controllers import paths
	from src.controllers import settings
	from src.controllers import load_const
	from src.controllers import themes
	from src.controllers import languages

	# 	- views
	from src.views import load_data
	from src.views import main_view

	# - models
	from src.models import labels
	from src.models import inputs
	from src.models import buttons
	from src.models import menus

	# script

	from src.script import graphs
	from src.script import video
	from src.script import crypt
	from src.script import read_data
	from src.script import maps

	# from src import root

except Exception as e:

	raise e


class Main:

	def __init__(self):
		
		self.BASE_DIR = os.getcwd()
		self.load_controllers()
		self.load_scripts()
		self.load_models()
		self.load_views()
		self.load_app()

	def __str__(self):
		
		return "main"


	# Initialisation des class controllers
	def load_controllers(self):

		self.path_controller = paths.Paths(self.BASE_DIR + "/res/data/paths.json", self.BASE_DIR)
		self.setting_controller = settings.Settings(self.path_controller.get_path('SETTINGS_PATH'))
		self.consts_controller = load_const.Load_Consts(self.path_controller.get_path("CONST_PATH"))
		self.theme_controller = themes.Theme(self.path_controller.get_path('THEME_PATH') + self.setting_controller.get_setting("theme") + ".json")	
		self.language_controller = languages.Language(self.path_controller.get_path('LANG_PATH') + self.setting_controller.get_setting("language") + ".json")	

		self.controllers = Controllers(
			self.BASE_DIR,
			self.path_controller, 
			self.setting_controller, 
			self.consts_controller,
			self.theme_controller, 
			self.language_controller
			)


	# Initialisation des class views
	def load_views(self):

		self.load_data = load_data.Load_Data_Window(self.controllers, self.models)
		self.main_view = main_view.Main_Window(self.controllers, self.models, self.scripts)
		self.views = Views(
			self.load_data,
			self.main_view
			)


	# Initialisation des class models
	def load_models(self):

		self.models = Models(
			labels.Labels(),
			inputs.Inputs(),
			buttons.Buttons(),
			menus.Menus()
			)

	# Initialisation des class scripts
	def load_scripts(self):
		
		self.graph_class = graphs.Graph()
		self.video_class = video.Video()
		self.decypt_class = crypt.Decrypt()
		self.read_data = read_data.Data_Reader(self.path_controller.get_path("FILES_DATA"))
		self.maps = maps.Map()

		self.scripts = Script(
			self.graph_class,
			self.video_class,
			self.decypt_class,
			self.read_data,
			self.maps
			)
 

	# Démarre l'application
	def load_app(self):
		
		self.app = root.Root(
			self.controllers, 
			self.models, 
			self.views,
			self.scripts
			)



# gère l'ensemble des models

class Controllers:


	def __init__(self, BASE_DIR, path_controller, setting_controller, consts_controller, theme_controller, language_controller):

		self.BASE_DIR = BASE_DIR

		self.path_controller = path_controller
		self.setting_controller = setting_controller
		self.consts_controller = consts_controller
		self.theme_controller = theme_controller
		self.language_controller = language_controller


	def __str__(self):

		return "Controller Class"



# gère l'ensemble des models  
 
class Models:


	def __init__(self, labels, inputs, buttons, menus):

		self.labels = labels
		self.inputs = inputs
		self.buttons = buttons
		self.menus = menus


	def __str__(self):

		return "Models Class"


# gère l'ensemble des models

class Views:


	def __init__(self, load_data, main_view):

		self.load_data = load_data
		self.main_view = main_view


	def __str__(self):

		return "Views Class"


# gère l'ensemblre des actions "backend" de l'application

class Script:


	def __init__(self, graphs, videos, decrypt, read_data, maps):

		self.graphs = graphs
		self.videos = videos
		self.decrypt = decrypt
		self.read_data = read_data
		self.maps = maps


	def __str__(self):
		
		return "Script class"


# Démarre le script
if __name__ == '__main__':
	print("start")
	main = Main()
