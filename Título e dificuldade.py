'''
Esse código foi um rascunho feito para a função que define a dificuldade
e cria a tela de título
'''

import pygame
import time
import random

pygame.init()
#%% Configuração da janela
# Configurações da janela do jogo
janela_comp=600
janela_alt=400
janela=pygame.display.set_mode((janela_comp,janela_alt))
def titulo():
    tela=True

    while tela:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    tela=False

                if event.key==pygame.K_1:
                    fps=10
                elif event.key==pygame.K_2:
                    fps=15
                elif event.key==pygame.K_3:
                    fps=30
                elif event.key==pygame.K_9:
                    fps=100
        
    
        janela.fill((0,0,0))
        fonte_tit=pygame.font.SysFont('comic sans', 50)
        tex_tit=fonte_tit.render('Jogo da Cobrinha', True, (255,255,255))
        janela.blit(tex_tit,(200,200))
        sel_font=pygame.font.SysFont('comic sans', 50)
        esc_font=pygame.font.SysFont('comic sans', 20)
        sel_texto=sel_font.render('Escolha a dificuldade: ',True,(255,255,255))
        facil_texto=sel_font.render('1 - Fácil',True,(255,255,255))
        medio_texto=sel_font.render('2 - Médio',True,(255,255,255))
        dif_texto=sel_font.render('3 - Difícil',True,(255,255,255))
        imp_texto=sel_font.render('9 - Impossível (É SÉRIO!)',True,(255,255,255))
        pygame.display.flip()  


titulo()
'''
def dificuldade():
    tela=True

    while tela:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    tela=False
    
    fps=0

    janela.fill((0,0,0))
    sel_font=pygame.font.SysFont('comic sans', 50)
    esc_font=pygame.font.SysFont('comic sans', 20)
    sel_texto=sel_font.render('Escolha a dificuldade: ',True,(255,255,255))
    facil_texto=sel_font.render('1 - Fácil',True,(255,255,255))
    medio_texto=sel_font.render('2 - Médio',True,(255,255,255))
    dif_texto=sel_font.render('3 - Difícil',True,(255,255,255))
    imp_texto=sel_font.render('9 - Impossível (É SÉRIO!)',True,(255,255,255))

    if event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                fps=10
            elif event.key==pygame.K_2:
                fps=15
            elif event.key==pygame.K_3:
                fps=30
            elif event.key==pygame.K_9:
                fps=100
    pygame.display.flip()
    '''