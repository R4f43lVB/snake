import pygame
from configurações import janela_comp,janela_alt,janela

def pontuacao(cor,fonte,tam,pontos):

    pygame.font.init()

    pont_font=pygame.font.SysFont(fonte,tam)

    surface=pont_font.render('Pontos: '+str(pontos),True,cor)

    pontos_rect=surface.get_rect()

    janela.blit(surface,pontos_rect)