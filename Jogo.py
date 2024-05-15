#%% importando bibliotecas e iniciando o pygame
import pygame
import time
import random

pygame.init()
#%% Configuração da janela
# Configurações da janela do jogo
janela_comp=600
janela_alt=400

# Configurações das paredes (o player morre quando encosta nas paredes)

janela=pygame.display.set_mode((janela_comp,janela_alt))
pygame.display.set_caption('Jogo da cobrinha')
fps=15

#%% Baixando assets
def baixar_assets():
    assets={}

    assets['corpo']=pygame.image.load('assets/EL cuerpo.png').convert_alpha()
    assets['corpo']=pygame.transform.scale(assets['corpo'],10,10)
    assets['cabeca']=pygame.image.load('assets/cabeça da minha cobra.png').convert_alpha()
    assets['rabo']=pygame.image.load('assets/Rabetão.png').convert_alpha()
    assets['virar']=pygame.image.load('assets/Corpo_virando.png').convert_alpha()
    assets['comida']=pygame.image.load('assets/Fruta.png').convert_alpha()
    assets['mundo']=pygame.image.load('assets/Background_final.png').convert()
    assets['mundo']=pygame.transform.scale(assets['mundo'],(janela_comp,janela_alt))
    
    return assets

assets=baixar_assets()

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

#%% Função do loop principal do jogo
def pontuacao(cor,fonte,tam,pontos):

    pygame.font.init()

    pont_font=pygame.font.SysFont(fonte,tam)

    surface=pont_font.render('Pontos: '+str(pontos),True,cor)

    pontos_rect=surface.get_rect()

    janela.blit(surface,pontos_rect)

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

#%% Definindo o jogo
while True:
    janela.fill((0,0,0))
    janela.blit(assets['mundo'],(0,0))
    pontuacao((255,255,255),'comic sans',20,pontos)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if sentido!='DIR':
                    prox_dir='ESQ'
            elif event.key==pygame.K_RIGHT:
                if sentido!='ESQ':
                    prox_dir='DIR'
            elif event.key==pygame.K_UP:
                if sentido!='BAIXO':
                    prox_dir='CIMA'
            elif event.key==pygame.K_DOWN:
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
    else:
        cobra_corpo.pop()

    
    if not fruta_spawn:
        fruta_pos=[random.randrange(1,(janela_comp//10))*10,
                    random.randrange(1,(janela_alt//10))*10]
        fruta_spawn=True

    # Desenhando a cobra:

    for pos in cobra_corpo:
        janela.blit(assets['corpo'],(pos[0],pos[1]))
    
    # desenha a fruta
    janela.blit(assets['comida'],(fruta_pos[0],fruta_pos[1]))

    pygame.display.update()

    clock.tick(fps)

    # Morre quando a cobra encosta em si mesma
    for corpo in cobra_corpo[1:]:
        if cobra_pos == list(corpo):
            pygame.quit()
            break

    # Game over

    if cobra_pos[0]<0 or cobra_pos[0]>janela_comp-10:
        pygame.quit()
        break
    elif cobra_pos[1]<0 or cobra_pos[1]>janela_alt-10:
        pygame.quit()
        break