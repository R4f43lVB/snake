import pygame
import time
import random

pygame.init()

# Configurações da janela do jogo
janela_comp=1080
janela_alt=600

# Configurações das paredes (o player morre quando encosta nas paredes)

janela=pygame.display.set_mode((janela_comp,janela_alt))
pygame.display.set_caption('Jogo da cobrinha')
fps=60

# Função que importa os assets da pasta de mesmo nome do repositório

def baixar_assets():
    assets={}

    assets['corpo']=pygame.image.load('assets/EL cuerpo.png').convert()
    assets['cabeca']=pygame.image.load('assets/cabeça da minha cobra.png').convert()
    assets['comida']=pygame.image.load('assets/Fruta.png').convert()
    return assets

# Posição inicial do jogador

p0_cab=[200,300] # POsição da cabeça
p0_corpo=[[200,300],
          [190,300],
          [180,300],
          [170,300]]
class snake(pygame.sprite.Sprite):
    def __init__(self,assets,grupos):

        pygame.sprite.Sprite.__init__(self)
        self.sprite=assets['corpo']
        self.rect=self.sprite.get_rect()
        self.rect.x=200
        self.rect.y=300
        self.speed=10
        self.direcao=''
        self.ir_para=self.direcao

class fruta(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.sprite=assets['comida']
        self.pos_x=random.randrange(1,(janela_comp//10)*10)
        self.pos_y=random.randrange(1,(janela_alt//10)*10)


def jogar(tela):
    clock=pygame.time.Clock()
    assets=baixar_assets()
    
    cobra=pygame.sprite.Group()
    tudo=pygame.sprite.Group()
    paredes=pygame.sprite.Group()

    
    
    grupos={}
    grupos['cobra']=cobra
    grupos['tudo']=tudo
    grupos['paredes']=paredes

    # Criando o player
    player=snake(assets,grupos)
    tudo.add(player)

    FINAL=0
    JOGANDO=1
    MORRENDO=2
    CRESCENDO=3
    estado=JOGANDO

    teclas={}
    pontos=0

    # O jogo para quando o estado muda
    while estado!=FINAL:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                estado=FINAL

            if estado==JOGANDO:
                # Se o jogador aperta alguma tecla:
                if event.type==pygame.KEYDOWN:
                    teclas[event.key]=True
                    if event.key==pygame.K_LEFT:
                        player.direcao='ESQ'
                    elif event.key==pygame.K_RIGHT:
                        player.direcao='DIR'
                    elif event.key==pygame.K_UP:
                        player.direcao='CIMA'
                    elif event.key==pygame.K_DOWN:
                        player.direcao='BAIXO'
        
        if player.ir_para=='CIMA' and player.direcao!='BAIXO':
            player.direcao='CIMA'
        elif player.ir_para=='BAIXO' and player.direcao!='CIMA':
            player.direcao='BAIXO'
        elif player.ir_para=='ESQ' and player.direcao!='DIR':
            player.direcao='ESQ'
        elif player.ir_para=='DIR' and player.direcao!='ESQ':
            player.diecao=='DIR'
            
        
        tudo.update()