import math
import pygame
from pygame.locals import *
import random
import time

#init do pygame
pygame.init()
screen = pygame.display.set_mode((785,550))
clock = pygame.time.Clock()
screen.fill((255,255,255))
pygame.display.set_caption("Cuide-C")
icon = pygame.image.load('miscelania/icon.png')
pygame.display.set_icon(icon)

#Placares
font = pygame.font.SysFont('forte',40)
placar_geral=0

#Tempo
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)

#Variáveis de música
Musica = True
Som = True

#Mapas/Elementos do Jogo
highest = 0
mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()
mapajogo2 = pygame.image.load("cenario/praca.png").convert()
mapajogo3 = pygame.image.load("cenario/JOGO3.png").convert()
fimdejogo = pygame.image.load("cenario/fim de jogo.png").convert_alpha()
pontuacao = pygame.image.load("cenario/pontuacao.png").convert_alpha()
relogio = pygame.image.load("miscelania/relogio.png").convert_alpha()
telainicial = pygame.image.load("cenario/Pagina inicial acesa.png").convert()
beep = pygame.mixer.Sound("miscelania/pop.mp3")

#Spirits
perscima = pygame.image.load("pers/pablitobandeja.png").convert_alpha()
botaoinst = pygame.image.load("miscelania/botaoinst.jpg").convert_alpha()
pablitocima = pygame.image.load("pers/pablitocima.png").convert_alpha()

#Elementos jogo 1
compras = pygame.image.load("miscelania/caixa_cheia.png").convert_alpha()

melancia = pygame.image.load("miscelania/melancia.png").convert_alpha()
maca = pygame.image.load("miscelania/maca.png").convert_alpha()
vegetal1 = pygame.image.load("miscelania/vegetal1.png").convert_alpha()
vegetal2 = pygame.image.load("miscelania/vegetal2.png").convert_alpha()
vegetal3 = pygame.image.load("miscelania/vegetal3.png").convert_alpha()
vegetal4 = pygame.image.load("miscelania/vegetal4.png").convert_alpha()

alimentos = [melancia, maca, vegetal1, vegetal2, vegetal3, vegetal4]

melancia_mol = pygame.image.load("miscelania/melancia_mol.png").convert_alpha()
maca_mol = pygame.image.load("miscelania/maca_mol.png").convert_alpha()
vegetal1_mol = pygame.image.load("miscelania/vegetal1_mol.png").convert_alpha()
vegetal2_mol = pygame.image.load("miscelania/vegetal2_mol.png").convert_alpha()
vegetal3_mol = pygame.image.load("miscelania/vegetal3_mol.png").convert_alpha()
vegetal4_mol = pygame.image.load("miscelania/vegetal4_mol.png").convert_alpha()
melancia_lim = pygame.image.load("miscelania/melancia_limpo.png").convert_alpha()
maca_lim = pygame.image.load("miscelania/maca_limpo.png").convert_alpha()
vegetal1_lim = pygame.image.load("miscelania/vegetal1_limpo.png").convert_alpha()
vegetal2_lim = pygame.image.load("miscelania/vegetal2_limpo.png").convert_alpha()
vegetal3_lim = pygame.image.load("miscelania/vegetal3_limpo.png").convert_alpha()
vegetal4_lim = pygame.image.load("miscelania/vegetal4_limpo.png").convert_alpha()


alimentos_molhados = [melancia_mol, maca_mol, vegetal1_mol, vegetal2_mol, vegetal3_mol, vegetal4_mol]
alimentos_limpos = [melancia_lim, maca_lim, vegetal1_lim, vegetal2_lim, vegetal3_lim, vegetal4_lim]

copoagua = pygame.image.load("miscelania/copoagua.png").convert_alpha()
instjogo1 = pygame.image.load("cenario/inst_jogo1.png").convert_alpha()
geladeira = pygame.mixer.Sound("miscelania/geladeira.mp3")
agua = pygame.mixer.Sound("miscelania/agua.ogg")
#Elementos jogo 2
instjogo2 = pygame.image.load("cenario/inst_jogo2.png").convert_alpha()
homem1 = pygame.image.load("pers/homem1.png").convert_alpha()
homem2 = pygame.image.load("pers/homem2.png").convert_alpha()
mulher1 = pygame.image.load("pers/mulher1.png").convert_alpha()
pablitocima_int = pygame.image.load("pers/pablitocima_int.png").convert_alpha()
PERDEVIDA = pygame.USEREVENT+2
vida_foto = pygame.image.load("pers/pablitoapoiado.png").convert_alpha()
vida = pygame.transform.scale(vida_foto, (58,53))
terra = pygame.mixer.Sound("miscelania/terra.mp3")
#Elementos jogo 3
SPAWN_VIRUS = pygame.USEREVENT + 1
instjogo3 = pygame.image.load("cenario/inst_jogo3.png").convert_alpha()
bigV = pygame.image.load("pers/vilao_planc.png").convert_alpha()
bigC = pygame.image.load("pers/vilao_bacilo.png").convert_alpha()
viruspeq = pygame.image.load("pers/viruspeq.png").convert_alpha()
facesh = pygame.image.load("pers/faceshield.png").convert_alpha()
pop = pygame.mixer.Sound("miscelania/pop.mp3")
     
#Músicas
imfine = pygame.mixer.music.load("miscelania/musica1.mp3")
pygame.mixer.music.play()


#MENU
def menu():
    #Variáveis bool que definem o andamento do menu
    Menu = True
    Controles = False
    Sobre = False
    opc1 = False
    opc2 = False
    opc3 = False
    global Musica
    global Som
    global highest
    #Imagens de Background
    global telainicial
    controles = pygame.image.load("cenario/controles.png").convert_alpha()
    sobre = pygame.image.load("cenario/sobre.png").convert_alpha()
    
    #Imagens
    cabeca = pygame.image.load("pers/pablitoapoiado.png").convert_alpha()
    cabeca2 = pygame.image.load("pers/cabeca.png").convert_alpha()

    while Menu:
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telainicial, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 260 and mouse_position[1] <= 300:
                    opc1 = True
                else:
                    opc1 = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 350 and mouse_position[1] <= 390:
                    opc2 = True
                else:
                    opc2 = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 430 and mouse_position[1] <= 480:
                    opc3 = True
                else:
                    opc3 = False
            if event.type == MOUSEBUTTONDOWN:
                #Botão de Música
                if mouse_position[0] >= 600 and mouse_position[0] <= 675 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == True and Som == True:
                    telainicial = pygame.image.load("cenario/Pagina inicial som.png").convert()
                    pygame.mixer.music.stop()
                    Musica = False
                elif mouse_position[0] >= 600 and mouse_position[0] <= 675 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == False and Som == True:
                    telainicial = pygame.image.load("cenario/Pagina inicial acesa.png").convert()
                    pygame.mixer.music.play()
                    Musica = True
                elif mouse_position[0] >= 600 and mouse_position[0] <= 675 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == False and Som == False:
                    telainicial = pygame.image.load("cenario/Pagina inicial musica.png").convert()
                    pygame.mixer.music.play()
                    Musica = True
                elif mouse_position[0] >= 600 and mouse_position[0] <= 675 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == True and Som == False:
                    telainicial = pygame.image.load("cenario/Pagina inicial Apagada.png").convert()
                    pygame.mixer.music.stop()
                    Musica = False
                #Botão de Som
                if mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == True and Som == True:
                    telainicial = pygame.image.load("cenario/Pagina inicial musica.png").convert()
                    Som = False
                elif mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == True and Som == False:
                    telainicial = pygame.image.load("cenario/Pagina inicial acesa.png").convert()
                    Som = True
                elif mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == False and Som == False:
                    telainicial = pygame.image.load("cenario/Pagina inicial som.png").convert()
                    Som = True
                elif mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 468 and mouse_position[1] <= 537 and Musica == False and Som == True:
                    telainicial = pygame.image.load("cenario/Pagina inicial Apagada.png").convert()
                    Som = False

                #Botões do Menu _
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 260 and mouse_position[1] <= 300 and Menu == True:
                    Menu = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 350 and mouse_position[1] <= 390 and Controles == False:
                    Controles = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and Controles == True:
                    Controles = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 430 and mouse_position[1] <= 480 and Sobre == False:
                    Sobre = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and Sobre == True:
                    Sobre = False

                if Som == True:
                    pygame.mixer.Sound.play(pop)
                
            
            #Hover Selecionado            
            if opc1:
                screen.blit(cabeca, (250,240))
            if opc2:
                screen.blit(cabeca2, (475,325))
            if opc3:
                screen.blit(cabeca, (250,420))
                


            if Controles:
                screen.blit(controles, (0,0))
            if Sobre:
                screen.blit(sobre, (0,0))
                
                high = font.render("Recorde: "+str(highest), True, (0,0,0))
                screen.blit(high, (300, 330))
                
                

            #printar tela
            pygame.display.update()
            clock.tick(30)

def minigames():
    placar = []
    jogos = [0,1,2]
    #Loop de minigames aleatórios
    for i in range(3):
        
        #definição aleatória do jogo
        jogoatual = random.choice(jogos)
        #jogoatual = 3
        #jogoatual = 2
        #jogoatual = 1
        
        
        #jogo 1 - Higienize seus alimentos
        global mapajogo1
        global perscima
        global compras
        global alimentos_molhados
        global alimentos
        global placar_geral
        global botaoinst
        global instjogo1
        global Som
        persx = 0
        persy = 0
        x = 0
        y = 0
        angle = 0
        bandeja_vazia = True
        bandeja_cont = ""
        pia_vazia = True
        pia_cont = -2
        placar_jogo1 = 0
        instr = True
        temporizador_1 = 30
        gastaragua = 2
            
            
        while jogoatual == 0:
            screen.blit(mapajogo1, (0,0))
            pers = pygame.transform.rotate(perscima, angle)
            if instr == False:
                screen.blit(pers, (x, y))
                
            if bandeja_vazia == False and angle==0 and bandeja_cont=="alimento":   
                screen.blit(alimentos[conteudo], (x+20, y+70))
            elif bandeja_vazia == False and angle==90 and bandeja_cont=="alimento":   
                screen.blit(alimentos[conteudo], (x+70, y+30))
            elif bandeja_vazia == False and angle==180 and bandeja_cont=="alimento":   
                screen.blit(alimentos[conteudo], (x+25, y-10))
            elif bandeja_vazia == False and angle==270 and bandeja_cont=="alimento":   
                screen.blit(alimentos[conteudo], (x-5, y+20))

            if bandeja_vazia == False and angle==0 and bandeja_cont=="alimento_molhado":   
                screen.blit(alimentos_molhados[conteudo], (x+20, y+70))
            elif bandeja_vazia == False and angle==90 and bandeja_cont=="alimento_molhado":   
                screen.blit(alimentos_molhados[conteudo], (x+70, y+30))
            elif bandeja_vazia == False and angle==180 and bandeja_cont=="alimento_molhado":   
                screen.blit(alimentos_molhados[conteudo], (x+25, y-10))
            elif bandeja_vazia == False and angle==270 and bandeja_cont=="alimento_molhado":   
                screen.blit(alimentos_molhados[conteudo], (x-5, y+20))

            if bandeja_vazia == False and angle==0 and bandeja_cont=="alimento_limpo":   
                screen.blit(alimentos_limpos[conteudo], (x+20, y+70))
            elif bandeja_vazia == False and angle==90 and bandeja_cont=="alimento_limpo":   
                screen.blit(alimentos_limpos[conteudo], (x+70, y+30))
            elif bandeja_vazia == False and angle==180 and bandeja_cont=="alimento_limpo":   
                screen.blit(alimentos_limpos[conteudo], (x+25, y-10))
            elif bandeja_vazia == False and angle==270 and bandeja_cont=="alimento_limpo":   
                screen.blit(alimentos_limpos[conteudo], (x-5, y+20))

            if bandeja_vazia == False and angle==0 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+20, y+70))
            elif bandeja_vazia == False and angle==90 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+70, y+30))
            elif bandeja_vazia == False and angle==180 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+25, y-10))
            elif bandeja_vazia == False and angle==270 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x-5, y+20))

            if instr == False:
                screen.blit(botaoinst, (690,470))

            mapajogo1.blit(compras, (380, 350))
            mouse_position = pygame.mouse.get_pos()
            if instr:
                screen.blit(instjogo1, (0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    if mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 470 and mouse_position[1] <= 545 and instr == False:
                        instr = True
                    else:
                        instr = False
                if event.type == KEYDOWN and instr == False:
                    if event.key == K_RIGHT:
                        persx += 4
                        angle = 90         
                    if event.key == K_LEFT:
                        persx += -4
                        angle = 270
                    if event.key == K_DOWN:
                        persy += 4
                        angle = 0
                    if event.key == K_UP:
                        persy += -4
                        angle = 180
                    if event.key == K_e:
                        bandeja_cont = ""
                        bandeja_vazia = True
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        persx = 0
                    if event.key == K_LEFT:
                        persx = 0
                    if event.key == K_DOWN:
                        persy = 0
                    if event.key == K_UP:
                        persy = 0
                if event.type == CLOCKTICK and instr == False:
                    temporizador_1 = temporizador_1 -1

            #barreiras sprite
            if x >= 785 - perscima.get_width():
                x = 785 - perscima.get_width()
            elif x < 120:
                x = 120
                    
            if y >= 450:
                y = 450
            elif y < 130:
                y = 130
                
            #Toca caixa de compras    
            if x >= 300 and x<= 500 and y >= 380 and y <= 530:
                y = 380
            if x >= 300 and x<= 500 and y >= 380 and y <= 530 and bandeja_vazia==True:
                y = 380
                bandeja_vazia = False
                bandeja_cont = "alimento"
                conteudo = random.randint(0,5)
            #Toca reservatorio agua
            if x <= 120 and y <= 510 and y>=400 and bandeja_vazia==True:
                bandeja_cont = "agua"
                bandeja_vazia = False
            #Toca pia
            if y <= 130 and x <= 440 and x>=350 and bandeja_vazia==False and pia_vazia==False and bandeja_cont=="alimento":
                bandeja_cont = "alimento_molhado"
                bandeja_vazia = False
                gastaragua -= 1
                
            if y <= 130 and x <= 440 and x>=350 and bandeja_vazia==False and bandeja_cont=="agua":
                mapajogo1 = pygame.image.load("cenario/cozinha_comagua.png").convert()
                bandeja_cont = ""
                pia_vazia = False
                bandeja_vazia = True
                if Som == True:
                    pygame.mixer.Sound.play(agua)
            #toca secador
            if y <= 130 and x <= 130 and x>=120 and bandeja_vazia==False and bandeja_cont=="alimento_molhado":
                bandeja_cont = "alimento_limpo"
                bandeja_vazia = False
            #toca geladeira
            if y <= 130 and x >= 600 and x <= 770 and bandeja_vazia==False and bandeja_cont=="alimento_limpo":
                bandeja_cont = ""
                bandeja_vazia = True
                placar_jogo1 += 1
                if Som == True:
                    pygame.mixer.Sound.play(geladeira)
            
            score1 = font.render(str(placar_jogo1), True, (0,0,0))
            screen.blit(score1, (735, 10))
            tempo = font.render(str(temporizador_1), True, (0,0,0))
            screen.blit(tempo, (650, 10))
            screen.blit(relogio, (615, 15))

            x += persx
            y += persy

            if temporizador_1 < 0:
                jogoatual += 100

            if gastaragua == 0:
                mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()
                pia_vazia = True
                gastaragua = 2

            pygame.display.update()
            clock.tick(30)
            

        if placar_jogo1 < 3:
            placar_jogo1 = placar_jogo1*20
        if placar_jogo1 >= 3:
            placar_jogo1 = placar_jogo1*25
        if placar_jogo1 == 0:
            placar_jogo1 = 10
        placar.append(placar_jogo1)
        placar_geral += placar_jogo1
        print(placar_jogo1)
        mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()
        



        #Jogo 2 - Distancie-se
        global mapajogo2
        placar_jogo2 = 0
        regra1 = True
        regra2 = False
        regra3 = False
        x = 10
        y = 410
        #angulos
        angulo_homem1 = 0
        angulo_homem1_2 = 0
        angulo_homem2 = 0
        angulo_homem2_2 = 0
        angulo_mulher1 = 0
        angulo_mulher1_2 = 0
        #posições iniciais
        mulher1x = 785 - mulher1.get_width()
        mulher1y = 520 - mulher1.get_height()/2
        mulher1_2x = 550
        mulher1_2y = 130 - mulher1.get_height()/2
        homem1x = 350
        homem1y = 0 - homem1.get_height()/2
        homem1_2x = 785 - homem1.get_width()
        homem1_2y = 360 - homem1.get_height()/2
        homem2x = 150
        homem2y = 350
        homem2_2x = 520 
        homem2_2y = 450
        def upanddown(direction, y, pos_final):
            angulo = 0
            if direction == "down":
                y += 1
                if y >= pos_final:
                    direction = "up"
            if direction == "up":
                angulo = 180
                y -= 1
                if y <= 0:
                    direction = "down"
            return y, angulo, direction

        def leftandright(direction, x, pos_final):
            angulo = 90
            if direction == "right":
                x += 1
                if x >= pos_final:
                    direction = "left"
            if direction == "left":
                angulo = 270
                x -= 1
                if x <= 150:
                    direction = "right"
            return x, angulo, direction

        def circle(direction, x, y, units):
            if direction == "down":
                angulo = 0
                y += 1
                if y >= units:
                    direction = "left"
            if direction == "left":
                angulo = 270
                x -= 1
                if x <= 600:
                    direction = "up"
            if direction == "up":
                angulo = 180
                y -= 1
                if y <= 350:
                    direction = "right"
            if direction == "right":
                angulo = 90
                x += 1
                if x >= 720:
                    direction = "down"
            return x, y, angulo, direction
        
        direction_down = "down"
        direction_up = "up"
        direction_left = "left"
        direction_right = "right"
        direction_circle = "down"
        direction_circle2 = "down"
        vidas = 3
        tangivel = True
        temporizador_2 = 30
                
        while jogoatual == 1:
            bottom = pygame.draw.line(screen, (255,0,0), (0, 350), (580,350), 5)
            assist1 = pygame.draw.line(screen, (0,0,0), (600, 350), (785,350), 5)
            assist2 = pygame.draw.line(screen, (255,255,255), (620, 130), (785,130), 10)
            assist3 = pygame.draw.line(screen, (255,50,255), (100, 150), (100,0), 5)


            rect = pygame.draw.rect(screen, (255,255,255), (x, y, 50, 65))
            rect2 = pygame.draw.rect(screen, (0,0,0), (homem2x, homem2y, 70, 85))
            rect3 = pygame.draw.rect(screen, (0,0,0), (homem2_2x, homem2_2y, 70, 85))
            rect4 = pygame.draw.rect(screen, (255,0,0), (homem1_2x, homem1_2y, 65, 50))
            rect5 = pygame.draw.rect(screen, (0,0,0), (homem1x, homem1y, 65, 50))
            rect6 = pygame.draw.rect(screen, (0,255,0), (mulher1x, mulher1y, 60, 60))
            rect7 = pygame.draw.rect(screen, (0,0,0), (mulher1_2x, mulher1_2y, 60, 60))

            
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    print(mouse_position)
                    if mouse_position[0] >= 710 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 75 and instr == False:
                        instr = True
                    else:
                        instr = False
                if event.type == KEYDOWN and instr == False:
                    if event.key == K_RIGHT:
                        persx += 4
                        angle = 90
                    if event.key == K_LEFT:
                        persx += -4
                        angle = 270
                    if event.key == K_DOWN:
                        persy += 4
                        angle = 0
                    if event.key == K_UP:
                        persy += -4
                        angle = 180
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        persx = 0
                    if event.key == K_LEFT:
                        persx = 0
                    if event.key == K_DOWN:
                        persy = 0
                    if event.key == K_UP:
                        persy = 0
                if event.type == PERDEVIDA:
                    tangivel = True
                if event.type == CLOCKTICK and instr == False:
                    temporizador_2 = temporizador_2 -1
                        
            mulher1rot = pygame.transform.rotate(mulher1, angulo_mulher1)
            mulher1_2rot = pygame.transform.rotate(mulher1, angulo_mulher1_2)
            homem1rot = pygame.transform.rotate(homem1, angulo_homem1)
            homem1_2rot = pygame.transform.rotate(homem1, angulo_homem1_2)
            homem2rot = pygame.transform.rotate(homem2, angulo_homem2)
            homem2_2rot = pygame.transform.rotate(homem2, angulo_homem2_2)
            spirit = pygame.transform.rotate(pablitocima, angle)
            spirit_int = pygame.transform.rotate(pablitocima_int, angle)
            
            #barreiras sprite
            if x >= 795 - pablitocima.get_width():
                x = 795 - pablitocima.get_width()
            elif x < 0:
                x = 0
                    
            if y >= 550 - pablitocima.get_height():
                y = 550 - pablitocima.get_height()
            elif y <= 0:
                y = 0

            #mapa
            if regra1:
                if x <= 600 and y <= 350:
                    y = 350
                if rect2.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
                if rect3.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
                if rect4.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
                if rect6.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
            if regra2:
                if x <= 620 and y <= 400 and y >= 80:
                    x = 620
                if rect4.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
                if rect6.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)

            if regra3:
                if y >= 120:
                    y = 120
                if rect5.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)
                if rect7.colliderect(rect) and tangivel:
                    vidas -= 1
                    tangivel = False
                    pygame.time.set_timer(PERDEVIDA, 1500)


                
            x += persx
            y += persy
            

            if instr:
                ########################################COMENTAR LINHA DE BAIXO DURANTE APRESENTAÇÃO
                screen.blit(mapajogo2, (0,0))
                screen.blit(instjogo2, (0,0))

            if instr == False:

                #definindo movimentação das pessoas
                homem1y, angulo_homem1, direction_down = upanddown(direction_down, homem1y, 120)
                mulher1_2y, angulo_mulher1_2, direction_up = upanddown(direction_up, mulher1_2y, 120)
                homem1_2x, homem1_2y, angulo_homem1_2, direction_circle = circle(direction_circle, homem1_2x, homem1_2y, 530-homem1.get_height())
                mulher1x, mulher1y, angulo_mulher1, direction_circle2 = circle(direction_circle2, mulher1x, mulher1y, 485)
                homem2x, angulo_homem2, direction_right = leftandright(direction_right, homem2x, 520)
                homem2_2x, angulo_homem2_2, direction_left = leftandright(direction_left, homem2_2x, 520)
                
                screen.blit(mapajogo2, (0,0))
                screen.blit(spirit, (x, y))
                screen.blit(botaoinst, (710,0))
                screen.blit(mulher1rot, (mulher1x, mulher1y))
                screen.blit(mulher1_2rot, (mulher1_2x, mulher1_2y))
                screen.blit(homem1rot, (homem1x, homem1y))
                screen.blit(homem2rot, (homem2x, homem2y))
                screen.blit(homem1_2rot, (homem1_2x, homem1_2y))
                screen.blit(homem2_2rot, (homem2_2x, homem2_2y))
                tempo = font.render(str(temporizador_2), True, (0,0,0))
                screen.blit(tempo, (235, 15))
                screen.blit(relogio, (200, 20))
                if tangivel == False:
                    screen.blit(spirit_int, (x,y))

            
            if bottom.collidepoint((x,y)):
                regra1 = True
            elif assist1.collidepoint((x,y)):
                regra1 = False
                regra2 = True
            elif assist2.collidepoint((x,y)):
                regra1 = False
                regra2 = False
                regra3 = True
            if assist3.collidepoint((x,y)) and vidas == 3:
                placar_jogo2 = 350
                jogoatual += 100
            if assist3.collidepoint((x,y)) and vidas == 2:
                placar_jogo2 = 300
                jogoatual += 100
            if assist3.collidepoint((x,y)) and vidas == 1:
                placar_jogo2 = 200
                jogoatual += 100
            if assist3.collidepoint((x,y)) and vidas == 0:
                placar_jogo2 = 100
                jogoatual += 100


            if vidas == 3:
                screen.blit(vida, (140,10))
            if vidas >= 2:
                screen.blit(vida, (80,10))
            if vidas >=1:
                screen.blit(vida, (20, 10))
            if vidas < 0 or temporizador_2 < 0:
                placar_jogo2 = 10
                jogoatual += 100

            
            pygame.display.update()
            clock.tick(30)


        placar_geral += placar_jogo2
        placar.append(placar_jogo2)




        
        #jogo 3 - Mantenha o virus longe:
        class Virus:
            def __init__(self , x, y, foto):
                self.x = x
                self.y = y
                self.foto = foto
                self.direcaox = random.choice([2,-2])
                self.direcaoy = random.choice([2,-2])
                if self.foto == bigV:
                    self.raio = 30 
                elif self.foto == bigC:
                    self.raio = 25
                elif self.foto == viruspeq:
                    self.raio = 10
        class Mouse:
            def __init__(self , x, y):
                self.x = x
                self.y = y
                self.raio = 40
        def colisao(mouse, virus):
            if virus.foto == bigV:
                xv = virus.x+25
                yv = virus.y+25
            elif virus.foto == bigC:
                xv = virus.x+20
                yv = virus.y+20
            elif virus.foto == viruspeq:
                xv = virus.x+10
                yv = virus.y+9
            distancia =  math.sqrt(((mouse.x-xv)**2)+((mouse.y-yv)**2))
            if (mouse.raio + virus.raio) >= distancia:
                return True
            else:
                return False
            
        temporizador_3 = 15
        spawn = True
        virus = []
        tipovirus = [bigV, bigC, viruspeq, bigV, bigC, bigV, bigC]
        x,y=0,0
        move_x, move_y = 0,0
        global instjogo3
        placar_jogo3 = 0

        
        while jogoatual == 2:
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    if mouse_position[0] >= 690 and mouse_position[0] <= 765 and mouse_position[1] >= 470 and mouse_position[1] <= 545 and instr == False:
                        instr = True
                    else:
                        instr = False
                if event.type == MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    x,y = mouse_position
                    mouse = Mouse(mouse_position[0]-5, mouse_position[1]-6)
                if event.type == SPAWN_VIRUS and instr == False:
                    virus.append(Virus(random.randint(0,770), random.randint(0,550), random.choice(tipovirus)))
                    virus.append(Virus(random.randint(0,770), random.randint(0,550), random.choice(tipovirus)))
                if event.type == CLOCKTICK and instr == False:
                    temporizador_3 = temporizador_3 -1
                 
            screen.blit(mapajogo3, (0,0))
            score2 = font.render(str(placar_jogo3), True, (0,0,0))
            screen.blit(score2, (735, 5))
            tempo = font.render(str(temporizador_3), True, (0,0,0))
            screen.blit(tempo, (50, 10))
            screen.blit(relogio, (15, 15))
            x += move_x
            y += move_y
            pygame.draw.circle(screen, (59, 131, 189), (x-5, y-6), 40, 0)
            for i in range(0, len(virus)):
                if virus[i].foto == bigV:
                    pygame.draw.circle(screen, (245, 221, 78), (virus[i].x+25, virus[i].y+25), 30, 0)
                if virus[i].foto == bigC:
                    pygame.draw.circle(screen, (255, 25, 25), (virus[i].x+20, virus[i].y+20), 25, 0)
                if virus[i].foto == viruspeq:
                    pygame.draw.circle(screen, (19, 56, 21), (virus[i].x+10, virus[i].y+9), 10, 0)

            
            if instr == False:
                screen.blit(botaoinst, (690,470)) 
                for i in range(0, len(virus)):
                    if virus[i].x >= 755 or virus[i].x <= 0:
                        virus[i].direcaox = virus[i].direcaox * -1

                    if virus[i].y >= 530 or virus[i].y <= 0:
                        virus[i].direcaoy = virus[i].direcaoy * -1

                    virus[i].y = virus[i].y + virus[i].direcaoy
                    virus[i].x = virus[i].x + virus[i].direcaox
            
            if spawn:
                spawn = False
                pygame.time.set_timer(SPAWN_VIRUS, 2000)

            for i in virus:
                screen.blit(i.foto, (i.x, i.y))
                if colisao(mouse, i):
                    if i.foto == viruspeq:
                        placar_jogo3 += 3
                    else:
                        placar_jogo3 += 1
                    if Som == True:
                        pygame.mixer.Sound.play(pop)
                    virus.remove(i)
                    pygame.display.flip()

                
            #definindo o fim do jogo
            if temporizador_3 == 0:
                jogoatual += 100


            if instr:
                screen.blit(instjogo3, (0,0))

            screen.blit(facesh,(x-35,y-35))
            pygame.display.update()
            clock.tick(30)

        placar_jogo3 = placar_jogo3*10
        placar_geral += placar_jogo3 
        placar.append(placar_jogo3)


        jogos.remove(jogoatual-100)
        print(jogos)


    #Mostrar pontuação na tela
    pontos = True
    global highest
    print(placar)
    while pontos:
        for i in placar:
            if i <= 0:
                placar.remove(i)
        screen.blit(telainicial, (0,0))
        screen.blit(pontuacao, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
                pontos = False


        score1 = font.render("Jogo 1:                      " + str(placar[0]), True, (0,0,0))
        screen.blit(score1, (175, 185))

        score2 = font.render("Jogo 2:                      " + str(placar[1]), True, (0,0,0))
        screen.blit(score2, (175, 250))

        score3 = font.render("Jogo 3:                      " + str(placar[2]), True, (0,0,0))
        screen.blit(score3, (175, 315))
        
        total = font.render("     Total:            " + str(placar_geral), True, (0,0,0))
        screen.blit(total, (175, 400))
        
        pygame.display.update()
    
    if placar_geral >= highest:
        highest = placar_geral
        
    screen.blit(fimdejogo, (0,0))
    pygame.display.update()




while True:
    menu()
    minigames()
    time.sleep(3)



