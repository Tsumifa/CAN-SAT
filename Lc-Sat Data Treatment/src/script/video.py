# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier video.py")
	import cv2 as cv
	import matplotlib.pyplot as plt

except Exception as e:
	raise e


# class liaison avec l'interface

class Video:


	# Liaison avec la class Motion filtering
	def video_motion_filtering(self, video_path):

		return Video_Motion_Filtering(video_path)




# Détourage des formes en mouvements sur la vidéo

class Video_Motion_Filtering:

	# charge la video et les composants nécéssaires pour le filtrage des mouvements 
	def __init__(self, video_path):

		self.video_path = video_path
		self.video = cv.VideoCapture(self.video_path)
		self.substractor = cv.createBackgroundSubtractorMOG2(20, 50)

		self.get_motion_filtering()

	# Détourage des formes
	def get_motion_filtering(self):

		# Recherche si la vidéo est toujours en cours:
		# 	- si oui, applique le détourage tant que la touche 'x' n'est pas pressée
		# 	- si non, relance la vidéo

		while True:
			return_value, frame = self.video.read()

			if return_value:
				mask = self.substractor.apply(frame)
				cv.imshow('Mask', mask)

				if cv.waitKey(5) == ord('x'):
					break

			else:
				self.video = cv.VideoCapture(self.video_path)

		cv.destroyAllWindows()
		self.video.release()
		

# Tracking d'objets

class Video_Object_Detection:

	def __init__(self, video_path):
		self.video_path = video_path


# Reconnaissance d'objets

class Video_Object_Recognition:

	def __init__(self):
		pass


print("Fin Chargement fichier video.py")