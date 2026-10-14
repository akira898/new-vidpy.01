import os 
from motor.render import game
import pygame

pygame.init()

pantalla = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Mi juego")
from check1 import check1
class file:
	def __init__(self,archive,line,lineInFile):
		self.archive=archive
		self.line=line
		self.lineInFile=lineInFile
codeOfTheGame={}
if not os.path.exists("project"):
	print("last one")
	os.makedirs("project")
	with open(os.path.join("project","script.vd"),"w")as code:
		code.write("")
archiveExtracting=file(os.path.join("project","script.vd"),0,0)
for i in os.listdir("project"):
	if i.endswith(".vd"):
		print("won")
		archiveExtracting.archive=i
		with open(os.path.join("project",archiveExtracting.archive),"r")as code:
			for line in code:
				c=line
				codeOfTheGame[archiveExtracting.line]=c
				#lines of the script read
				print(codeOfTheGame[archiveExtracting.line])
				archiveExtracting.line+=1
				#lines of the file read
				archiveExtracting.lineInFile+=1
			archiveExtracting.lineInFile=0
				
if check1(codeOfTheGame):
	print("sex")
	game(pantalla)