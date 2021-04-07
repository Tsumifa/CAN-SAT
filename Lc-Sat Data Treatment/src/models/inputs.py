# -*- coding: utf-8 -*-

try:
	print("Chargement fichier inputs.py")
	import tkinter as tk
	from tkinter import ttk
	from tkinter import filedialog

except Exception as e:
	raise e


# class de liaison entre les différents models input

class Inputs:


	def __init__(self):
		
		self.entry = Entry()

	def __str__(self):

		return "Inputs class"


# Champs de saisie de text

class Entry:


	def create_widget(self, parent):
		
		entry = ttk.Entry(parent)
		return entry


print("Fin Chargement fichier inputs.py")

