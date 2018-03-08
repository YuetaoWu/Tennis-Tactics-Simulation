# -*- coding: utf-8 -*-

'''
Created on Thrusday Mar 08 14:36:00 2018

@author: Yuetao Wu

'''

''' 
	Define three object:players,ball,game


'''
class Player:

	def __init__(self,playerName,*scorePara,*posPara,**statePara):
		self.scorePara = scorePara
		self.posPara = posPara
		self.statePara = statePara
		self.playerName = playerName 
		print('Creat a new Player {0}'.format(self.playerName))

	def Move2Ball(self,ballPara):
		pass

	def HitBall(self,ballPara):
		# use scorePara posPara & statePara
		pass


class Ball:

	def __init__(self,*posPara,*dynamicPara,**distrbPara):
		self.posPara = posPara
		self.dynamicPara = dynamicPara
		self.distrbPara = distrbPara
		print('Creat a new Ball')
	
	def ballFly():
		pass

class Game:

	def __init__(self,Player1,Player2,Ball):
		self.Player1 = Player1
		self.Player2 = Player2
		self.Ball = Ball
	def gameSatrt():
		pass
	def gameEnd():
		pass





