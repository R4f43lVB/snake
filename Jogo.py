#%% importando bibliotecas e iniciando o pygame
import pygame
import time
import random

pygame.init()
#%% Configuração da janela
# Configurações da janela do jogo
janela_comp=1000
janela_alt=600

# Configurações das paredes (o player morre quando encosta nas paredes)

janela=pygame.display.set_mode((janela_comp,janela_alt))
pygame.display.set_caption('Jogo da cobrinha')
fps=60

#%% Baixando assets
def baixar_assets():
    assets={}

    assets['corpo']=pygame.image.load('assets/EL cuerpo.png').convert()
    assets['cabeca']=pygame.image.load('assets/cabeça da minha cobra.png').convert()
    assets['comida']=pygame.image.load('assets/Fruta.png').convert()
    assets['mundo']=pygame.image.load('assets/background.png').convert_alpha()
    
    return assets

assets=baixar_assets()

#%% Cobra
sentido='DIR'
prox_dir=sentido

cobra_pos=[100,50]
cobra_corpo=[(100,50,assets['cabeca'],sentido),
             (90,50,assets['corpo'],sentido),
             (80,50,assets['corpo'],sentido),
             (70,50,assets['corpo'],sentido)]

#%% Frutas

fruta_pos=(random.randrange(1,(janela_comp//10))*10,
           random.randrange(1,(janela_alt//10))*10)
fruta_spawn=True

#%% Função do loop principal do jogo

def pontuacao(cor,fonte,tam,pontos):

    pont_font=pygame.font.SysFont(fonte,tam)

    surface=pont_font.render('Pontos: '+str(pontos),True,cor)

    pontos_rect=surface.get_rect()

    janela.blit(surface,pontos_rect)

def fim_de_jogo(pontos,recorde):
    fonte=pygame.font.SysFont('times new roman',50)
    surf=fonte.render('Você marcou: ', str(pontos), True,color=(255,0,0))
    time.sleep(1)
    if pontos>recorde:
        rec=fonte.render('NOVO RECORDE!!')
    
    fdj_rect=surf.get_rect()

    fdj_rect.pos=(janela_comp/2,janela_alt/2)

    janela.blit(surf,fdj_rect)
    pygame.display.flip()

def jogar(tela):
    clock=pygame.time.Clock()
    assets=baixar_assets()

    # Posição do jogador

    #%% Criação dos grupos
    cobra=pygame.sprite.Group()
    tudo=pygame.sprite.Group()
    paredes=pygame.sprite.Group()
    
    grupos={}
    grupos['cobra']=cobra
    grupos['tudo']=tudo
    grupos['paredes']=paredes

    #%% Criando o player


    FINAL=0
    JOGANDO=1
    MORRENDO=2
    estado=JOGANDO

    teclas={}
    pontos=0
    tem_fruta=True

    #%% Definindo o jogo
    while estado!=FINAL:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                estado=FINAL
            janela.fill('black')
            pygame.display.flip()

            if estado==JOGANDO:
                # Se o jogador aperta alguma tecla:
                if event.type==pygame.KEYDOWN:
                    teclas[event.key]=True
                    if event.key==pygame.K_LEFT:
                        prox_dir='ESQ'
                    elif event.key==pygame.K_RIGHT:
                        prox_dir='DIR'
                    elif event.key==pygame.K_UP:
                        prox_dir='CIMA'
                    elif event.key==pygame.K_DOWN:
                        prox_dir='BAIXO'
                

        
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
        else:
            cobra_corpo.pop()
        
        if not fruta_spawn:
            fruta_pos=(random.randrange(1,(janela_comp//10))*10,
                       random.randrange(1,(janela_alt//10))*10)
        fruta_pos=True
        janela.fil(0,0,0)

        for pos in cobra_corpo:
            pygame.draw.rect(janela,(0,255,0),pygame.Rect(pos[0],pos[1],10,10))
        
        pygame.draw.rect(janela,(255,255,255),pygame.Rect(fruta_pos[0],fruta_pos[1],10,10))

        # Game over

        if cobra_pos[0]<0 or cobra_pos[0]>janela_comp-10:
            fim_de_jogo()
        elif cobra_pos[1]<0 or cobra_pos[1]>janela_alt-10:
            fim_de_jogo()

jogar(janela)