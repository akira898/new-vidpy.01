import pygame
from motor import gameState
from motor.gameState import TextIn,dialoguePosition

def game(pantalla):
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render(TextIn.DialogueIn, True, (255, 255, 255))
    
    ejecutando = True

    while ejecutando:
        texto = fuente.render(TextIn.DialogueIn, True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                gameState.dialoguePosition+=1
                print("click")
        pantalla.fill((30, 30, 30))
        pantalla.blit(texto, (250, 275))
        pygame.display.flip()