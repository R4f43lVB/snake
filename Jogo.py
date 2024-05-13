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
sentido=''
prox_dir=sentido

cobra_pos=[300,150]
cobra_corpo=[(300,150,assets['cabeca'],sentido),
             (290,150,assets['corpo'],sentido),
             (280,150,assets['corpo'],sentido),
             (270,150,assets['corpo'],sentido)]



#%% Frutas
'''
fruta_pos=[random.randrange(1,(janela_comp//10))*10,
           random.randrange(1,(janela_alt//10))*10]
fruta_spawn=True
print(fruta_pos)
'''
#%% Função do loop principal do jogo

def pontuacao(cor,fonte,tam,pontos):

    pont_font=pygame.font.SysFont(fonte,tam)

    surface=pont_font.render('Pontos: '+str(pontos),True,cor)

    pontos_rect=surface.get_rect()

    janela.blit(surface,pontos_rect)

def fim_de_jogo(pontos,recorde):
    fonte=pygame.font.SysFont('times new roman',50)
    surf=fonte.render('Você marcou: ', str(pontos),True)
    time.sleep(1)
    if pontos>recorde:
        rec=fonte.render('NOVO RECORDE!!')
    
    fdj_rect=surf.get_rect()


    janela.blit(surf,fdj_rect)
    pygame.display.flip()




clock=pygame.time.Clock()
assets=baixar_assets()

fruta_pos=[random.randrange(1,(janela_comp//10))*10,
            random.randrange(1,(janela_alt//10))*10]
fruta_spawn=True

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
rec=1000
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
        fruta_spawn=True

    for pos in cobra_corpo:
        pygame.draw.rect(janela,(0,255,0),pygame.Rect(pos[0],pos[1],10,10))
    
    pygame.draw.rect(janela,(255,255,255),pygame.Rect(fruta_pos[0],fruta_pos[1],10,10))

    # Game over

    if cobra_pos[0]<0 or cobra_pos[0]>janela_comp-10:
        pygame.quit()
    elif cobra_pos[1]<0 or cobra_pos[1]>janela_alt-10:
        pygame.quit()

# Morre quando a cobra encosta em si mesma
for corpo in cobra_corpo[1:]:
    if cobra_pos[0]==corpo[0] and cobra_pos[1]==corpo[1]:
        fim_de_jogo(pontos,rec)

pontuacao(pontos,(255,255,255),'comic sans',20)
pygame.display.update()
clock.tick(fps)
        
