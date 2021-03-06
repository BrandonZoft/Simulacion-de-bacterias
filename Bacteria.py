import pygame, sys
from pygame.locals import *
import random

class Bacteria(pygame.sprite.Sprite):
	def __init__(self, position_x, position_y, gram=True):
		""" posicion de la bacteria en la simulacion
			gram: definir si la bacteria es gram positiva:True o negativa:False"""
		pygame.sprite.Sprite.__init__(self)

		#sprite de la bacteria
		self.sprite = pygame.image.load("sprites/bacteria.png")
		self.tamano = random.randint(10,30)
		self.sprite = pygame.transform.scale(self.sprite, (self.tamano, self.tamano))
		self.sprite_de_bacteria = self.sprite.get_rect()

		#variables de la bacteria
		self.sprite_de_bacteria.centerx = position_x
		self.sprite_de_bacteria.centery = position_y
		self.gram = gram
		self.salud = 100
		self.energia = random.randint(0, 100)
		self.reproduccion = False
		self.pared_celular = 100 if self.gram else 8
		self.metabolismo = round(random.random(), 1)
		self.porcentage_de_adaptacion = random.randint(1, 7) / 10
		self.adaptacion = 0.0
		self.tiempo = 0
		self.consumo_de_energia = round(random.random() * -1, 1)

	def termorecepcion(self, temperatura):
		if temperatura < 5:
			self.salud = 0
		elif temperatura > 5 and temperatura < 15:
			self.salud -= 0.1
		elif temperatura > 15 and temperatura < 30:
			self.salud -= 0.03
		elif temperatura > 30 and temperatura < 40:
			self.salud = self.salud
		elif temperatura > 40 and temperatura < 50:
			self.salud -= 0.03
		elif temperatura > 50 and temperatura < 60:
			self.salud -= 0.1
		elif temperatura > 60: 
			self.salud = 0

	def sensacion_de_humedad(self, porcentage):
		pass

	def sesacion_de_acidez(self, pH):
		#pH 7 es neutro, < es acido, > 7 es base
		if pH > 7.0 and pH < 8.0:
			self.salud = self.salud
		elif pH > 4.0 and pH < 7.0:
			self.salud -= 0.3 
		elif pH > 1.0 and pH < 4.0:
			self.salud -= 0.5
		elif pH > 8.0 and pH < 11.0:
			self.salud -= 0.3
		elif pH > 11.0 and pH < 14.0:
			self.salud -= 0.5

	def ingerir_nutrientes(self, nutrinte):
		if self.energia < 100 and nutrinte < 10:
			self.energia += nutrinte * self.metabolismo
		elif self.energia > 100: 
			self.energia = 90

	def receptor_de_antibiotico(self, daño):
		pass

	def verificar_reproduccion(self):
		if self.energia > 95 and self.energia < 100 and self.adaptacion > 90:
			self.energia -= 50
			return True
		else: return False

	def verificar_energia(self):
		self.energia += self.consumo_de_energia - 0.1
		return self.energia
	
	def verificar_salud(self):
		pass

	def establecer_tiempo(self):
		self.adaptacion += self.porcentage_de_adaptacion 

	def colocar_bacteria(self, window):
		window.blit(self.sprite, self.sprite_de_bacteria)

	def cordenadas(self):
		return self.sprite_de_bacteria.centerx, self.sprite_de_bacteria.centery

	def movimiento(self):
		self.sprite_de_bacteria.centerx += random.randint(-1, 1) 
		self.sprite_de_bacteria.centery += random.randint(-1, 1)
