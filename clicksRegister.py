import pygame 
from motor.render import  ejecutando
dialIn=0
while ejecutando:
	for event in pygame.event.get():
	   	 if event.type==pygame.QUIT:
	   	 	ejecutando=False 
            if event.type == pygame.MOUSEBUTTONDOWN:
            	dialIn += 1