#%% importando bibliotecas e iniciando o pygame
import pygame
import time
from baixar_assets import baixar_assets
from configurações import janela_alt,janela_comp,janela
from pont import pontuacao
from titulo import titulo
import random
from pygame.time import wait

pygame.init()
#%% Configuração da janela
# Configurações da janela do jogo

# Configurações das paredes (o player morre quando encosta nas paredes)
while True:
    #janela=pygame.display.set_mode((janela_comp,janela_alt))
    pygame.display.set_caption('Jogo da cobrinha')
    fps=15

    assets=baixar_assets()
    #Sons e Musica do jogo 
    pygame.mixer.music.load('assets/musica_jogo6.mp3')
    pygame.mixer.music.play(-1)  # Loop infinito para rodar o jogo inteiro
    som_comer = pygame.mixer.Sound('assets/comer_fruta.mp3')# Som quando a cobra comer a fruta 
    som_colisao = pygame.mixer.Sound('assets/game-over-31.mp3')# Som quando a cobra encostar nela mesma ou nas paredes

    #%% Cobra
    sentido='DIR'
    prox_dir=sentido

    cobra_pos=[300,150]
    cobra_corpo=[(300,150),
                (290,150),
                (280,150),
                (270,150)]



    #%% Frutas

    fruta_pos=[random.randrange(1,(janela_comp//10))*10,
            random.randrange(1,(janela_alt//10))*10]
    fruta_spawn=True

    #%% Pontuação
    '''
    def pontuacao(cor,fonte,tam,pontos):

        pygame.font.init()

        pont_font=pygame.font.SysFont(fonte,tam)

        surface=pont_font.render('Pontos: '+str(pontos),True,cor)

        pontos_rect=surface.get_rect()

        janela.blit(surface,pontos_rect)
    '''
    clock=pygame.time.Clock()
    assets=baixar_assets()

    fruta_pos=[random.randrange(1,(janela_comp//10))*10,
                random.randrange(1,(janela_alt//10))*10]
    fruta_spawn=True

    # Posição do jogador

    # Estados
    FINAL=0
    JOGANDO=1
    MORRENDO=2
    estado=JOGANDO

    pontos=0
    tem_fruta=True


    fps = titulo()
    #%% Definindo o jogo
    while True:



        janela.fill((0,0,0))
        janela.blit(assets['mundo'],(0,0))
        pontuacao((0,0,0),'open sans',20,pontos)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:

                pygame.quit()
                break

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    if sentido!='DIR':
                        prox_dir='ESQ'

                elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    if sentido!='ESQ':
                        prox_dir='DIR'
                elif event.key==pygame.K_UP or event.key==pygame.K_w:
                    if sentido!='BAIXO':
                        prox_dir='CIMA'
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    if sentido!='CIMA':
                        prox_dir='BAIXO'

                
            
        # Atualizando a direção
        sentido=prox_dir

        # Movimentando a cobra
        if sentido=='CIMA':
            cobra_pos[1]-=10
        elif sentido=='BAIXO':
            cobra_pos[1]+=10
        elif sentido=='ESQ':
            cobra_pos[0]-=10
        elif sentido=='DIR':
            cobra_pos[0]+=10
        

    # Fazendo a cobra crescer a cada vez que encosta em uma fruta:
        cobra_corpo.insert(0,list(cobra_pos))
        if cobra_pos[0]==fruta_pos[0] and cobra_pos[1]==fruta_pos[1]:
            pontos+=100
            fruta_spawn=False
            som_comer.play()
        else:
            cobra_corpo.pop()

        
        if not fruta_spawn:
            fruta_pos=[random.randrange(1,(janela_comp//10))*10,
                        random.randrange(1,(janela_alt//10))*10]
            fruta_spawn=True

        # Desenhando a cobra:

        for i,pos in enumerate(cobra_corpo):
            # Caso a cobra mude de direção, muda o sprite
            
            if list(pos)==cobra_pos:
                # Cabeça da cobra
                if sentido=='CIMA':
                    janela.blit(assets['cabeca_cima'],(pos[0],pos[1]))
                elif sentido=='BAIXO':
                    janela.blit(assets['cabeca_baixo'],(pos[0],pos[1]))
                elif sentido=='ESQ':
                    janela.blit(assets['cabeca_esq'],(pos[0],pos[1]))
                elif sentido=='DIR':
                    janela.blit(assets['cabeca_dir'],(pos[0],pos[1]))
            elif i==len(cobra_corpo)-1:
                # Rabo
                if sentido=='CIMA':
                    janela.blit(assets['rabo_cima'],(pos[0],pos[1]))
                elif sentido=='BAIXO':
                    janela.blit(assets['rabo_baixo'],(pos[0],pos[1]))
                elif sentido=='ESQ':
                    janela.blit(assets['rabo_esq'],(pos[0],pos[1]))
                else:
                    janela.blit(assets['rabo_dir'],(pos[0],pos[1]))
            
            else:
                # Corpo
                if sentido in ['BAIXO','CIMA']:
                    janela.blit(assets['corpo_v'],(pos[0],pos[1]))
                else:
                    janela.blit(assets['corpo_h'],(pos[0],pos[1]))
        # desenha a fruta
        janela.blit(assets['comida'],(fruta_pos[0],fruta_pos[1]))

        pygame.display.update()

        clock.tick(fps)

        # Morre quando a cobra encosta em si mesma
        Game_over=False
        for corpo in cobra_corpo[1:]:
            if cobra_pos == list(corpo):
                Game_over=True
                break
            
        # Game over

        if cobra_pos[0]<0 or cobra_pos[0]>janela_comp-10 or Game_over==True:
            som_colisao.play()
            wait(2000)
            #pygame.quit()
            break
        elif cobra_pos[1]<0 or cobra_pos[1]>janela_alt-10:
            som_colisao.play()
            wait(2000)
            #pygame.quit()
            break