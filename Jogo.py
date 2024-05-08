import pygame
import time
import random

pygame.init()

# Configurações da janela do jogo
janela_comp=1080
janela_alt=720

janela=pygame.display.set_mode((janela_comp,janela_alt))
pygame.display.set_caption('Jogo da cobrinha')
fps=60

# Função que importa os assets da pasta de mesmo nome do repositório

def baixar_assets():
    assets={}

    assets['corpo']=pygame.image.load('/assets/EL cuerpo.png').convert()
    assets['cabeca']=pygame.image.load('/assets/cabeça da minha cobra.png')
    assets['comida']=pygame.image.load('/assets/Fruta.png')
    return assets

class snake_head(pygame.sprite.Sprite):
    def __init__(self,assets):

        pygame.sprite.Sprite.__init__(self)
        self.sprite=assets['corpo']
        