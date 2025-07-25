print('Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3')

import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/john1/OneDrive/Documentos/Cursos/Python/Script/Meu mundo Python 1/teste.mp3')
pygame.mixer.music.play()
input("Pressione Enter para parar...")
pygame.mixer.music.stop()


