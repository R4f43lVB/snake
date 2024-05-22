import pygame
from configurações import janela
def titulo():
        tela=True

        #define fps padrão
        fps=15

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
                        fps=70

            janela.fill((0,145,145))
            fonte_tit=pygame.font.SysFont('comic sans', 50)
            tex_tit=fonte_tit.render('Jogo da Cobrinha', True, (255,255,255))
            sel_font=pygame.font.SysFont('comic sans', 35)
            esc_font=pygame.font.SysFont('comic sans', 25)
            sel_texto=sel_font.render('Escolha a dificuldade: ',True,(255,255,255))
            facil_texto=esc_font.render('1 - Fácil',True,(255,255,255))
            medio_texto=esc_font.render('2 - Médio',True,(255,255,255))
            dif_texto=esc_font.render('3 - Difícil',True,(255,255,255))
            imp_texto=esc_font.render('9 - Impossível (É SÉRIO!)',True,(255,255,255))
            next_texto=sel_font.render('Agora aperte Enter',True,(255,255,255))
            janela.blit(tex_tit,(100,50))
            janela.blit(sel_texto,(70,130))
            janela.blit(facil_texto,(70,180))
            janela.blit(medio_texto,(70,210))
            janela.blit(dif_texto,(70,240))
            janela.blit(imp_texto,(70,270))
            janela.blit(next_texto,(70,300))
                    
            pygame.display.flip()

        return fps