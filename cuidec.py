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

#Mapas de Jogo
mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()
mapajogo3 = pygame.image.load("cenario/JOGO3.png").convert()
fimdejogo = pygame.image.load("cenario/fim de jogo.png").convert_alpha()


#Spirits
perscima = pygame.image.load("pers/pablitobandeja.png").convert_alpha()


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

alimentos_molhados = [melancia_mol, maca_mol, vegetal1_mol, vegetal2_mol, vegetal3_mol, vegetal4_mol]

copoagua = pygame.image.load("miscelania/copoagua.png").convert_alpha()

#Elementos jogo 3
SPAWN_VIRUS = pygame.USEREVENT + 1

bigV = pygame.image.load("pers/vilao_planc.png").convert_alpha()
bigC = pygame.image.load("pers/vilao_bacilo.png").convert_alpha()
viruspeq = pygame.image.load("pers/viruspeq.png").convert_alpha()
facesh = pygame.image.load("pers/faceshield.png").convert_alpha()
        
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
    #Imagens de Background
    telainicial = pygame.image.load("cenario/Pagina inicial acesa.png").convert()
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
                

            #printar tela
            pygame.display.update()
            clock.tick(30)

def minigames():
    #Loop de minigames aleatórios
    for i in range(3):
    
        #definição aleatória do jogo
        jogoatual = random.randint(0,1)
        print(jogoatual)
        #jogo 1 - Higienize seus alimentos
        global mapajogo1
        global perscima
        global compras
        global alimentos_molhados
        global alimentos
        global placar_geral
        persx = 0
        persy = 0
        x = 0
        y = 0
        angle = 0
        bandeja_vazia = True
        bandeja_cont = ""
        pia_vazia = True
        pia_cont = -2
        placar_jogo1=0

        
        while jogoatual == 0:
            screen.blit(mapajogo1, (0,0))

            pers = pygame.transform.rotate(perscima, angle)
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

            if bandeja_vazia == False and angle==0 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+20, y+70))
            elif bandeja_vazia == False and angle==90 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+70, y+30))
            elif bandeja_vazia == False and angle==180 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x+25, y-10))
            elif bandeja_vazia == False and angle==270 and bandeja_cont=="agua":   
                screen.blit(copoagua, (x-5, y+20))

            mapajogo1.blit(compras, (380, 350))

            
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    jogoatual = 100
                if event.type == KEYDOWN:
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
                
            if y <= 130 and x <= 440 and x>=350 and bandeja_vazia==False and bandeja_cont=="agua":
                mapajogo1 = pygame.image.load("cenario/cozinha_comagua.png").convert()
                bandeja_cont = ""
                pia_vazia = False
                bandeja_vazia = True
                gastaragua = 2

            
            score1 = font.render(str(placar_jogo1), True, (0,0,0))
            screen.blit(score1, (735, 20))
            

            x += persx
            y += persy


            pygame.display.update()
            clock.tick(30)
            
        mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()
        #jogo 3 - Mantenha o virus longe:
        class Virus:
            def __init__(self , x, y, foto):
                self.x = x
                self.y = y
                self.foto = foto
                self.direcaox = random.choice([2,-2])
                self.direcaoy = random.choice([2,-2])
        def colisao(virus, mousex, mousey):
            distancia =  (virus.x - virus.getwidth()/2) + (mousex - facesh.getwidth()/2)  
            if (virus.getwidth()/2 - facesh.getwidth()/2) >= distancia:
                return True
            else:
                return False
            
        temporizador = 15
        spawn = True
        virus = []
        tipovirus = [bigV, bigC, viruspeq, bigV, bigC, bigV, bigC]
        x,y=0,0
        move_x, move_y = 0,0

        
        while jogoatual == 1:
            screen.blit(mapajogo3, (0,0))
            
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    jogoatual = 100
                if event.type == MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    x,y = mouse_position
                if event.type == SPAWN_VIRUS:
                    virus.append(Virus(random.randint(0,785), random.randint(0,550), random.choice(tipovirus)))
                    virus.append(Virus(random.randint(0,785), random.randint(0,550), random.choice(tipovirus)))
                if event.type == CLOCKTICK:
                    temporizador = temporizador -1


            x += move_x
            y += move_y

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
                #if colisao(i, mouse_position[0], mouse_position[1]):
                    #del i
                
            #definindo o fim do jogo
            if temporizador == 0:
                break



            screen.blit(facesh,(x-35,y-35))
            pygame.display.update()
            clock.tick(30)


    screen.blit(fimdejogo, (0,0))
    pygame.display.update()




while True:
    menu()
    minigames()
    time.sleep(3)


