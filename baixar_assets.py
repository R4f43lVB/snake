import pygame
from configurações import janela_comp,janela_alt

def baixar_assets():
    assets={}

    assets['corpo_v']=pygame.image.load('assets/EL cuerpo.png').convert_alpha()
    assets['corpo_v']=pygame.transform.scale(assets['corpo_v'],(15,15))
    assets['corpo_h']=pygame.transform.rotate(assets['corpo_v'],90)
    assets['cabeca_cima']=pygame.image.load('assets/cabeça da minha cobra.png').convert_alpha()
    assets['cabeca_cima']=pygame.transform.scale(assets['cabeca_cima'],(15,15))
    assets['cabeca_baixo']=pygame.transform.rotate(assets['cabeca_cima'],180)
    assets['cabeca_esq']=pygame.transform.rotate(assets['cabeca_cima'],90)
    assets['cabeca_dir']=pygame.transform.rotate(assets['cabeca_cima'],270)
    assets['rabo_cima']=pygame.image.load('assets/Rabetão.png').convert_alpha()
    assets['rabo_cima']=pygame.transform.scale(assets['rabo_cima'],(15,15))
    assets['rabo_baixo']=pygame.transform.rotate(assets['rabo_cima'],180)
    assets['rabo_esq']=pygame.transform.rotate(assets['rabo_cima'],90)
    assets['rabo_dir']=pygame.transform.rotate(assets['rabo_cima'],270)
    assets['virar']=pygame.image.load('assets/Corpo_virando.png').convert_alpha()
    assets['comida']=pygame.image.load('assets/Fruta.png').convert_alpha()
    assets['comida']=pygame.transform.scale(assets['comida'],(15,15))
    assets['mundo']=pygame.image.load('assets/Background_final.png').convert()
    assets['mundo']=pygame.transform.scale(assets['mundo'],(janela_comp,janela_alt))

    return assets