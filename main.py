# from cmath import sqrt
# from turtle import position
# from warnings import catch_warnings
# from numpy import mat, rec
# import pygame,os,json,scipy.ndimage,sys
import pygame,os,json,sys
from pygame.locals import *
# from module import json_open
import modules.TextManager as TM

#initialisation pygame
pygame.init()
#FPS clock
clock=pygame.time.Clock()

#taille ecran
screen=pygame.display.set_mode()
x,y=screen.get_size()
print("x : ",x," y : ",y)
pygame.quit()

#surface écran
#taille=(1000,600)
width_screen=x-20
height_screen=y-50
taille=(width_screen,height_screen)
screen=pygame.display.set_mode(taille,pygame.RESIZABLE)
print("resizable : ",pygame.RESIZABLE)

#taille ecran par défaut   screen=pygame.display.set_mode()
x,y=screen.get_size()
#voire taille ecran
print("taille ecran : ",(x,y))

#titre fenêtre
pygame.display.set_caption("Fanorona Malagasy")

#icon fanorona
pygame_icon=pygame.image.load(os.path.join("image","laka_logo.PNG"))
pygame.display.set_icon(pygame_icon)


# vato=[
#         [2, 2, 0, 2, 2, 2, 2, 2, 2],
#         [0, 1, 0, 2, 1, 0, 1, 1, 2],
#         [2, 0, 0, 1, 0, 0, 0, 0, 2],
#         [0, 1, 1, 2, 2, 1, 2, 1, 0],
#         [0, 0, 2, 2, 2, 0, 2, 2, 2]
#     ]
# vato=[
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]
vato=[
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 1, 2, 1, 0, 2, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

run=True
moving=False
clic=False
winner=False

player_in_game=1
joueur1=1
joueur2=2

color_joueur2="white"
color_j2="manga"

color_joueur1="green"
color_j1="maintso"

color_joueur="white"
color_j="manga"

#list adversair à eliminer 
elimin=[]

#list deplacement pièces
deplace=[]

#selection piece en cours
piece_seleted=False


# vector initialisatoin
mouse_pos = pygame.math.Vector2()
mouse_clic = pygame.math.Vector2()
piece_selected = pygame.math.Vector2(0, 0)

exeption = {(1, 0) : [[0, 1], [2, 1]], (3, 0) : [[2, 1], [4, 1]],
            (4, 1) : [[3, 0], [3, 2]], (4, 3) : [[3, 2], [3, 4]],
            (3, 4) : [[2, 3], [4, 3]], (1, 4) : [[0, 3], [2, 3]],
            (0, 3) : [[1, 2], [1, 4]], (0, 1) : [[1, 0], [1, 2]],
            (2, 1) : [[1, 0], [3, 0], [1, 2], [3, 2]],
            (3, 2) : [[2, 1], [4, 1], [2, 3], [4, 3]],
            (2, 3) : [[1, 2], [3, 2], [1, 4], [3, 4]],
            (1, 2) : [[0, 1], [2, 1], [0, 3], [2, 3]]}

while run:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

#lakapanorona
    #bg color
    marron=(197,133,75)
    mainty=(0,0,0)
    screen.fill(marron)
    #trace rectangle
    pygame.draw.rect(screen,mainty,pygame.Rect( (200,100) ,(800,400) ),10)
    #trace ligne
    pygame.draw.line(screen,(mainty),(600,100 ),(600,495),8)
    pygame.draw.line(screen,(mainty),(205,105 ),(600,495),10)
    pygame.draw.line(screen,(mainty),(605,495 ),(995,105),10)
    pygame.draw.line(screen,(mainty),(205,495 ),(600,105),10)
    pygame.draw.line(screen,(mainty),(605,105 ),(995,495),10)
    pygame.draw.line(screen,(mainty),(200,300 ),(995,300),8)
    pygame.draw.line(screen,(mainty),(400,100 ),(400,495),8)  
    pygame.draw.line(screen,(mainty),(800,105 ),(800,495),8)
    pygame.draw.line(screen,(mainty),(205,300),(400,105 ),10)
    pygame.draw.line(screen,(mainty),(205,300 ),(405,495),10)
    pygame.draw.line(screen,(mainty),(400,495 ),(800,105),10)
    pygame.draw.line(screen,(mainty),(800,105 ),(995,300),10)
    pygame.draw.line(screen,(mainty),(800,495),(995,300),10)
    pygame.draw.line(screen,(mainty),(400,105 ),(800,495),10)
    pygame.draw.line(screen,(mainty),(200,205 ),(995,205),8)
    pygame.draw.line(screen,(mainty),(200,400 ),(1000,400),8)
    pygame.draw.line(screen,(mainty),(300,100 ),(300,500),8)
    pygame.draw.line(screen,(mainty),(500,495 ),(500,100),8)
    pygame.draw.line(screen,(mainty),(700,100 ),(700,495),8)
    pygame.draw.line(screen,(mainty),(900,500 ),(900,100),8)
    #trace cercle
    pygame.draw.circle(screen,(0,0,0),(600,300 ),15)  

#Joueur qui joue    
    #affiche mijanona
    rect_mijanona = pygame.draw.rect(screen,mainty,pygame.Rect( (1065,30) ,(250,80) ),0)
    rect_rejouer = pygame.draw.rect(screen,mainty,pygame.Rect( (1065,130) ,(250,80) ),0)
    pygame.font.init()
    font=pygame.font.SysFont("Arial",50)
    font2=pygame.font.SysFont("Arial",30)
    text1=font.render("ijanona",True,"red")
    text2=font2.render("IVERINA  ADY",True,"white")
    rect1=text1.get_rect(topleft=(1120,40))
    rect2=text2.get_rect(topleft=(1110,150))
    screen.blit(text1,rect1)
    screen.blit(text2,rect2)

    #Fonction affiche joueur
    def bouton_clic(text, x, y, color, size):
        pygame.display.get_surface().blit(pygame.font.SysFont("Times New Roman", size, "").render(text, False, color), (x, y))

    #Fonction clic mijanano puis changement de joeur
    def mijanona(player_in_game):
        deplace=[]
        if player_in_game==1:
            return (2,"green","maintso",deplace)
        else :        
            return (1,"white","fotsy",deplace)
    
    def rejouer(vato):
        deplace=[]
        return vato,deplace

    mouse_pos_x = pygame.mouse.get_pos()[0]
    mouse_pos_y = pygame.mouse.get_pos()[1] 
    #test position mijanona sy clic eo
    test_1=rect1.collidepoint(mouse_pos_x, mouse_pos_y)
    test_2=pygame.mouse.get_pressed()[0]
    if test_1 and test_2:        
        # loko_manja=(238,150,100)
        # rect_mijanona = pygame.draw.rect(screen,marron,pygame.Rect( (1060,30) ,(250,80) ),8)
        player_in_game,color_joueur, color_j,deplace = mijanona(player_in_game)
        color_joueur = str(color_joueur)
        print("joueur : ",player_in_game)
        print("couleur : ",color_joueur)
        event=pygame.event.wait()
    if test_1 :        
        rect_mijanona = pygame.draw.rect(screen,marron,pygame.Rect( (1065,30) ,(250,80) ),8)

    #bouton REJOUER
    test_1=rect2.collidepoint(mouse_pos_x, mouse_pos_y)
    test_2=pygame.mouse.get_pressed()[0]
    if test_1 and test_2:  
        vato=[
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 1, 0, 2, 1, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]      
        (vato,deplace)=rejouer(vato)
        print("vato")
        event=pygame.event.wait(1)
    if test_1 :        
        # rect_mijanona = pygame.draw.rect(screen,marron,pygame.Rect( (1060,30) ,(210,80) ),8)
        rect_rejouer = pygame.draw.rect(screen,marron,pygame.Rect( (1065,130) ,(250,80) ),10)
    #affiche joueur en cours
    test1=0
    test2=0
    i=4
    while i>=0 :
        j=8
        while j>=0:
            if vato[i][j]==1:
                test1+=1
            elif  vato[i][j]==2:
                test2+=1
            j-=1    
        i-=1
    if test1==0:
        print(f"Player {color_j1} nandresy")
        color_j=color_j1
        color_joueur=color_joueur1
        winner=True
    elif test2==0:
        print(f"Player {color_j2} nandresy")  
        color_j=color_j2
        color_joueur=color_joueur2
        winner=True                
    else:
        winner=False              
    if winner==True:
        bouton_clic(f"Mpilalao {color_j} nandresy", 200, 10, color_joueur , 50)
    else:        
        bouton_clic(f"Mpilalao {color_j} mandeha zao", 200, 10, color_joueur , 50)


#Gestion de clic gauche qui est le variable l puis vato séléctionné
    l,m,r=pygame.mouse.get_pressed()
    if l:
        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        clic=True
        selected_piece = True

    #limite surface clicable avec clic gauche
    platformRect = pygame.Rect(160, 60, 110*8, 120*4)
    if platformRect.collidepoint(mouse_pos.x, mouse_pos.y) :        
        mouse_clic.x = ((mouse_pos.x - 150 ) // 100)
        mouse_clic.y = ((mouse_pos.y - 50 ) // 100)
    #pièce selectionné 
    piece_selectedX = int(mouse_clic.x)
    piece_selectedY = int(mouse_clic.y)
    # print(f"pieces en cour selectionner : {piece_selectedX},{piece_selectedY}")

    s_y = ((piece_selectedY *  100) + 100) - 120
    s_x = ((piece_selectedX *  100) + 100) - 120    
    #color pièce sélectionné
    if vato[int(piece_selectedY)][int(piece_selectedX)] == joueur1 and player_in_game == joueur1: 
        color = "grey"
    elif vato[int(piece_selectedY)][int(piece_selectedX)] == joueur2 and player_in_game == joueur2: 
        color = "black"
    else: color = None

#Clic gauche séléctionne pièce puis cercle puis chemin
    # pygame.event.wait(1)
    # def selection_piece(mouse_pos.x,mouse_pos.y,clic,color):
    if clic and platformRect.collidepoint(mouse_pos.x, mouse_pos.y) and color:
        cercle_selected=pygame.draw.circle(screen, color, (s_x + 220, s_y + 120), 35, 5)    
        #position x,y avec coordonné
        x_pos_mat = piece_selectedX 
        y_pos_mat = piece_selectedY 
        piece_seleted=True

    #Mat mistoque ireo liste lakabe 14
        # Mat=[(1,1), (1,3), (1,5), (1,7),(2, 2),(2,4),(2,6),(3,1), (3,3), (3,5), (3,7)]
        Mat=[(1,1), (3,1), (5,1), (7,1),(2, 2),(4,2),(6,2),(1,3), (3,3), (5,3), (7,3)]
        Chemin=[]
        chemin_valide=[]    
    #stoque chemin futur
    #chemin valide en vert
        for enum_colonne_mat,colonne_mat in enumerate(Mat):
            for enum_ligne_mat, ligne_mat in enumerate(colonne_mat):
                # print(f"mat[{enum_ligne_mat}][{enum_colonne_mat}] : {colonne_mat}")        
                if (x_pos_mat,y_pos_mat) in Mat :
                    if x_pos_mat>y_pos_mat:
                        debut_X  = x_pos_mat - 1
                        fin_X    = x_pos_mat + 2
                        debut_Y  = y_pos_mat - 1
                        fin_Y    = y_pos_mat + 2

                    elif x_pos_mat<y_pos_mat:
                        debut_X = x_pos_mat - 1 
                        fin_X   = x_pos_mat + 2
                        debut_Y = y_pos_mat - 1
                        fin_Y   = y_pos_mat + 2

                    else:                        
                        debut_X = x_pos_mat - 1 
                        fin_X   = y_pos_mat +2
                        debut_Y = debut_X
                        fin_Y   = fin_X
                        
                    for xx in range(debut_X,fin_X,1):
                        for yy in range(debut_Y,fin_Y,1):                            
                            for enum_colonne,colonne_vato in enumerate(vato):
                                for enum_ligne,ligne_vato in enumerate(colonne_vato):
                                    element_ligne_vato=vato[enum_colonne][enum_ligne]
                                    test=(enum_ligne,enum_colonne)
                                    if (x_pos_mat,y_pos_mat)!=(xx,yy) and  element_ligne_vato==0 :
                                        # print("test : ",test)                                         
                                        # print(f"vato [{enum_ligne }][{enum_colonne}]  : {element_ligne_vato}")
                                        if test not in chemin_valide:
                                            chemin_valide.append(test)
                                    if (x_pos_mat,y_pos_mat)!=(xx,yy) :
                                        if (xx, yy) not in Chemin:
                                                Chemin.append((xx, yy) )
                                            

            #ok
            #Affiche les chemin futurs
                # if (x_pos_mat,y_pos_mat)==(3, 3) :
                if (x_pos_mat,y_pos_mat)==Mat[enum_colonne_mat] : 
                    # print(f"position piece : {(y_pos_mat,x_pos_mat)}")
                    if (y_pos_mat,x_pos_mat) not in deplace:
                        deplace.append((y_pos_mat,x_pos_mat))
                    for enum_ligne,ligne_vato in enumerate(vato):
                        for enum_colonne,colonne_vato in enumerate(ligne_vato):    
                                  
                            for id_chemin,ligne_chemin in enumerate(Chemin):
                                #affiche chemin valide
                                if ligne_chemin in chemin_valide :
                                    if (ligne_chemin[1],ligne_chemin[0]) not in deplace :
                                        # print(f"ligne_chemin {(ligne_chemin[1],ligne_chemin[0])} xxx {deplace}")
                                        cercle_x = ((ligne_chemin[0] *  100) + 300) - 120     
                                        cercle_y = ((ligne_chemin[1] *  100) - 100) - 120                
                                        chemin_futur=pygame.draw.circle(screen, "green", (cercle_x + 20, cercle_y + 320), 35, 5)
                                    
                                    #chemin selectionner puis deplacement pièces    
                                        mouse_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                        chemin_mouse_clic = pygame.math.Vector2(((mouse_position.x - 150) // 100), ((mouse_position.y - 50) // 100))
                                        pygame.event.wait(1)
                                        if pygame.mouse.get_pressed()[0] and chemin_futur.collidepoint(mouse_position.x, mouse_position.y)  : 
                                            # elimin=[]
                                            print("clic chemin futur")
                                            (chemin_clic_x,chemin_clic_y)=chemin_mouse_clic
                                            if (chemin_clic_y,chemin_clic_x) not in deplace:
                                                print("deplace")
                                                difference = pygame.math.Vector2( chemin_mouse_clic.y - (piece_selectedY ), chemin_mouse_clic.x - (piece_selectedX ))
                                                print(f"difference : {difference}")
                                                # print(f"difference : y_{difference.y},x_{difference.x}")
                                                print(f"mouse clic : {chemin_mouse_clic.x},{chemin_mouse_clic.y}")
                                                print(f" pièce selectionner : {piece_selectedX},{piece_selectedY}")
                                                print(f"mouse clic coor vato   :{int(chemin_mouse_clic.y)} , {int(chemin_mouse_clic.x)}")
                                                print(f"pièce select coor vato :y_{piece_selectedY} , x_{piece_selectedX}")
                                                
                                                #stoque clic farany
                                                clic_farany_x=int(chemin_mouse_clic.y)
                                                clic_farany_y=int(chemin_mouse_clic.x)
                                                difference_coordonne_x=(chemin_mouse_clic.x-piece_selectedX)
                                                difference_coordonne_y=(chemin_mouse_clic.y-piece_selectedY)
                                                print(f"player in game : {player_in_game}")
                                                
                                            # ( difference_coorodonne (-1,-1))
                                                if (difference_coordonne_y==-1 and difference_coordonne_x==-1):
                                                    elimin=[]
                                                    entre_elimin=True
                                                    i=0
                                                    while entre_elimin:  
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i)>=0 and int(mouse_clic.x-difference_coordonne_x-i)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i), int(mouse_clic.x-difference_coordonne_x-i))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"vato elimine ok1[{x}][{y}]= {vato[x][y]}")                                                        
                                                        except:pass  
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i-1)>=0 and int(mouse_clic.x-difference_coordonne_x-i-1)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i-1), int(mouse_clic.x-difference_coordonne_x-i-1))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"vato elimine ok2[{x}][{y}]= {vato[x][y]}")                                                        
                                                        except:pass  
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i+1)>=0 and int(mouse_clic.x-difference_coordonne_x-i+1)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x-i+1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x-i+1)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+1), int(mouse_clic.x-difference_coordonne_x-i+1))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"vato elimine ok3[{x}][{y}]= {vato[x][y]}")
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)]!=0):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+2), int(mouse_clic.x-difference_coordonne_x-i+2))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"vato elimine ok4[{x}][{y}]= {vato[x][y]}")
                                                        except:pass                                            
                                                        try:
                                                            while (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)==player_in_game]
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)]==0
                                                                and pygame.event.wait(1)):
                                                                print("dona")
                                                                entre_elimin=False
                                                        except:entre_elimin=False
                                                        # try:
                                                        #     while (vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x-i-1)==player_in_game]
                                                        #         and vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x-i-1)]==0
                                                        #         and pygame.event.wait(1)):
                                                        #         print("dona1")
                                                        #         entre_elimin=False
                                                        # except:entre_elimin=False 
                                                        # try:
                                                        #     while (vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x-i+1)==player_in_game]
                                                        #         and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x-i+1)]==0
                                                        #         and pygame.event.wait(1)):
                                                        #         print("dona2")
                                                        #         entre_elimin=False
                                                        # except:entre_elimin=False                                                         
                                                        i+=1                

                                                if (difference_coordonne_y==1 and difference_coordonne_x==1):
                                                    elimin=[]
                                                    entre_elimin=True
                                                    i=0
                                                    while entre_elimin:  
                                                        if (int(mouse_clic.y-difference_coordonne_y-i+2)>=0 and int(mouse_clic.x-difference_coordonne_x-i+2)>=0):
                                                            try:       
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+2), int(mouse_clic.x-difference_coordonne_x-i+2))
                                                                    if (x>=0,y>=0) not in elimin:
                                                                        elimin.append((x,y))
                                                            except:pass 
                                                        try:
                                                            while (vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)!=player_in_game]
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x-i+2)]!=0
                                                                and pygame.event.wait(5)):
                                                                entre_elimin=False
                                                        except:entre_elimin=False   
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i+4)>=0 and int(mouse_clic.x-difference_coordonne_x-i+4)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i+4)][int(mouse_clic.x-difference_coordonne_x-i+4)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+4)][int(mouse_clic.x-difference_coordonne_x-i+4)]!=0
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x-i+3)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x-i+3)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+4), int(mouse_clic.x-difference_coordonne_x-i+4))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                        except:pass 
                                                        try:
                                                            if (int(mouse_clic.y-difference_coordonne_y-i)>=0 and int(mouse_clic.x-difference_coordonne_x-i)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i), int(mouse_clic.x-difference_coordonne_x-i))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                        except:pass
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i+3)>=0 and int(mouse_clic.x-difference_coordonne_x-i+3)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x-i+3)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x-i+3)]!=0):
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+3), int(mouse_clic.x-difference_coordonne_x-i+3))
                                                                    if (x>=0,y>=0) not in elimin:
                                                                        elimin.append((x,y))
                                                        except:pass                                           
                                                        try:
                                                            while (vato[int(mouse_clic.y-difference_coordonne_y-i+4)][int(mouse_clic.x-difference_coordonne_x-i+4)!=player_in_game]
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+4)][int(mouse_clic.x-difference_coordonne_x-i+4)]!=0
                                                                and pygame.event.wait(5)):
                                                               entre_elimin=False
                                                        except:entre_elimin=False                                                     
                                                        i+=1                                       

                                                #(y=1, x=-1)
                                                if (difference_coordonne_y==1 and difference_coordonne_x==-1):
                                                    elimin=[]
                                                    entre_elimin=True
                                                    i=0
                                                    while entre_elimin:  
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i+1)>=0 and int(mouse_clic.x-difference_coordonne_x+i-1)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]!=0):
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+1), int(mouse_clic.x-difference_coordonne_x+i-1))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"l11 vato[{x}][{y}]:{vato[x][y]}")
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]!=0):
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y-i-1), int(mouse_clic.x-difference_coordonne_x+i+1))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"ll_1 vato[{x}][{y}]:{vato[x][y]}")
                                                                    # if (int(mouse_clic.y-difference_coordonne_y-i)>=0 and int(mouse_clic.x-difference_coordonne_x+i)>=0):
                                                                    #     if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=player_in_game
                                                                    #     and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x +i)]!=0 
                                                                    #     and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]!=player_in_game
                                                                    #     and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]!=0):
                                                                    #         (x,y)=(int(mouse_clic.y-difference_coordonne_y-i), int(mouse_clic.x-difference_coordonne_x+i))
                                                                    #         if (x,y) not in elimin:
                                                                    #             elimin.append((x,y))
                                                                    #             print(f"T1 vato[{x}][{y}]:{vato[x][y]}")
                                                                    # (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+1), int(mouse_clic.x-difference_coordonne_x+i-1))
                                                                    # if (x,y) not in elimin:
                                                                    #     elimin.append((x,y))
                                                                    #     print(f"l1 vato[{x}][{y}]:{vato[x][y]}")
                                                        except:pass      
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y+i)>=0 and int(mouse_clic.x-difference_coordonne_x-i)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0 ):
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y+i+2)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y+i+2)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=0 ):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y+i), int(mouse_clic.x-difference_coordonne_x-i))
                                                                        print(f"el_111 vato[{x-1}][{y+2}]:{vato[x-1][y+2]}")
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y+i), int(mouse_clic.x-difference_coordonne_x-i))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"el_11 vato[{x}][{y}]:{vato[x][y]}")
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=0):
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=0):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y+i+1), int(mouse_clic.x-difference_coordonne_x-i-1))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"ell_2 vato[{x}][{y}]:{vato[x][y]}")
                                                        except:pass    
                                                        # try:       
                                                        #     if (int(mouse_clic.y-difference_coordonne_y+i)>=0 and int(mouse_clic.x-difference_coordonne_x-i)>=0):
                                                        #         if (vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                        #         and vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=0 ):
                                                        #             if (vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                        #             and vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i)]!=0 ):
                                                        #                 (x,y)=(int(mouse_clic.y-difference_coordonne_y+i), int(mouse_clic.x-difference_coordonne_x-i))
                                                        #                 print(f"el_111 vato[{x-1}][{y+2}]:{vato[x-1][y+2]}")

                                                        #             (x,y)=(int(mouse_clic.y-difference_coordonne_y+i), int(mouse_clic.x-difference_coordonne_x-i))
                                                        #             if (x,y) not in elimin:
                                                        #                 elimin.append((x,y))
                                                        #                 print(f"el_11 vato[{x}][{y}]:{vato[x][y]}")
                                                        #         if (vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=player_in_game
                                                        #         and vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=0):
                                                        #             if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=player_in_game
                                                        #             and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=0):
                                                        #                 (x,y)=(int(mouse_clic.y-difference_coordonne_y+i+1), int(mouse_clic.x-difference_coordonne_x-i-1))
                                                        #                 if (x,y) not in elimin:
                                                        #                     elimin.append((x,y))
                                                        #                     print(f"ell_2 vato[{x}][{y}]:{vato[x][y]}")
                                                        # except:pass                                                        
                                                        try:
                                                            while (vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)==player_in_game]
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]==0
                                                                and pygame.event.wait(5)):
                                                                print(f"l2 vato{[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]} : {vato[int(mouse_clic.y-difference_coordonne_y-i+1)][int(mouse_clic.x-difference_coordonne_x+i-1)]}")
                                                                entre_elimin=False
                                                        except:entre_elimin=False                                                         
                                                        i+=1
                                                    

                                                #(y=-1, x=1)
                                                if (difference_coordonne_y==-1 and difference_coordonne_x==1):
                                                    elimin=[]
                                                    entre_elimin=True
                                                    i=0
                                                    while entre_elimin:
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i-1)>=0 and int(mouse_clic.x-difference_coordonne_x+i+1)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]!=0 ):
                                                                    
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y-i-2)][int(mouse_clic.x-difference_coordonne_x+i+2)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y-i-2)][int(mouse_clic.x-difference_coordonne_x +i+2)]!=0 ):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y-i-2), int(mouse_clic.x-difference_coordonne_x+i+2))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"el2 vato[{x}][{y}]:{vato[x][y]}")
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i-1), int(mouse_clic.x-difference_coordonne_x+i+1))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"el1 vato[{x}][{y}]:{vato[x][y]}")
                                                        except:pass   
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y-i)>=0 and int(mouse_clic.x-difference_coordonne_x+i)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i)][int(mouse_clic.x-difference_coordonne_x+i)]!=0 ):
                                                                    
                                                                    # if (vato[int(mouse_clic.y-difference_coordonne_y-i-2)][int(mouse_clic.x-difference_coordonne_x+i+2)]!=player_in_game
                                                                    # and vato[int(mouse_clic.y-difference_coordonne_y-i-2)][int(mouse_clic.x-difference_coordonne_x +i+2)]!=0 ):
                                                                    #     (x,y)=(int(mouse_clic.y-difference_coordonne_y-i-2), int(mouse_clic.x-difference_coordonne_x+i+2))
                                                                    #     if (x,y) not in elimin:
                                                                    #         elimin.append((x,y))
                                                                    #         print(f"el2 vato[{x}][{y}]:{vato[x][y]}")
                                                                    (x,y)=(int(mouse_clic.y-difference_coordonne_y-i), int(mouse_clic.x-difference_coordonne_x+i))
                                                                    if (x,y) not in elimin:
                                                                        elimin.append((x,y))
                                                                        print(f"el1 vato[{x}][{y}]:{vato[x][y]}")
                                                        except:pass     
                                                        try:       
                                                            if (int(mouse_clic.y-difference_coordonne_y+i)>=0 and int(mouse_clic.x-difference_coordonne_x-i)>=0):
                                                                if (vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x-i)]!=player_in_game
                                                                and vato[int(mouse_clic.y-difference_coordonne_y+i)][int(mouse_clic.x-difference_coordonne_x -i)]!=0 ):
                                                                    # if (vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x+i-3)]!=player_in_game
                                                                    # and vato[int(mouse_clic.y-difference_coordonne_y-i+3)][int(mouse_clic.x-difference_coordonne_x +i-3)]!=0 ):
                                                                    # (x,y)=(int(mouse_clic.y-difference_coordonne_y-i+3), int(mouse_clic.x-difference_coordonne_x+i-3))
                                                                    # if (x,y) not in elimin:
                                                                    #     elimin.append((x,y))
                                                                    #     print(f"el3 vato[{x}][{y}]:{vato[x][y]}")
                                                                    if (vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x-i-1)]!=player_in_game
                                                                    and vato[int(mouse_clic.y-difference_coordonne_y+i+1)][int(mouse_clic.x-difference_coordonne_x -i-1)]!=0 ):
                                                                        (x,y)=(int(mouse_clic.y-difference_coordonne_y+i), int(mouse_clic.x-difference_coordonne_x-i))
                                                                        if (x,y) not in elimin:
                                                                            elimin.append((x,y))
                                                                            print(f"el44 vato[{x}][{y}]:{vato[x][y]}")
                                                        except:pass                                                                                                                 
                                                        try:
                                                            while (vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)==player_in_game]
                                                                and vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]==0
                                                                and pygame.event.wait(5)):
                                                                print(f" vato{[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]} : {vato[int(mouse_clic.y-difference_coordonne_y-i-1)][int(mouse_clic.x-difference_coordonne_x+i+1)]}")
                                                                print("dona5")
                                                                entre_elimin=False
                                                        except:entre_elimin=False    
                                                        # try:
                                                        #     while (vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x+i-2)==player_in_game]
                                                        #         and vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x+i-2)]==0
                                                        #         and pygame.event.wait(5)  ):
                                                        #         print(f" vato{[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x+i-2)]} : {vato[int(mouse_clic.y-difference_coordonne_y-i+2)][int(mouse_clic.x-difference_coordonne_x+i-2)]}")
                                                        #         entre_elimin=False
                                                        # except:entre_elimin=False                                                    
                                                        i+=1
                                                
                                                i=len(elimin)
                                                print(f"i : {i} elimin : {elimin}")                                    
                                                if i==0:
                                                    vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                    vato[piece_selectedY][piece_selectedX]=0
                                                    deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                                    # print(f"{(chemin_clic_y,chemin_clic_x)} deplace ajout : {deplace}")
                                            
                            #après clic sur chemin futur 

                                if elimin!=[] and (difference_coordonne_y==1 and difference_coordonne_x==-1) :
                                # or (difference_coordonne_y==1 and difference_coordonne_x==1)):        
                                    for i in range(0,int(len(elimin)+1)):
                                        if i>0:
                                            try:                              
                                                cercle_y = ((elimin[i-1][0] *  100) + 100) 
                                                cercle_x = ((elimin[i-1][1] *  100) + 200)  
                                                pygame.event.wait(1)
                                                piece_elimin_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                                piece_elimine=pygame.draw.circle(screen, "red", (cercle_x  , cercle_y ), 35, 5)
                                                if piece_elimine.collidepoint(piece_elimin_position.x, piece_elimin_position.y) and pygame.mouse.get_pressed()[0] :        
                                                    # pygame.event.wait(1)                                           
                                                    mouse_clic.x = ((piece_elimin_position.x - 150 ) // 100)
                                                    mouse_clic.y = ((piece_elimin_position.y - 50 ) // 100)
                                                    piece_selected_elimin_x=int(mouse_clic.x)
                                                    piece_selected_elimin_y=int(mouse_clic.y)

                                                    #elimine pièces 
                                                    entre_elimin1=True
                                                    while entre_elimin1:
                                                        ii=4
                                                        while ii>=0 :
                                                            jj=8
                                                            while jj>=0:
                                                                # if difference==(-1,1):
                                                                if (ii,jj)==elimin[i-1]: 
                                                                    # (x : -1 , y : 1)
                                                                    if ( 5>ii-1>-1   and 9>jj+1>-1 and vato[int(ii-1)][int(jj+1)]!=player_in_game
                                                                    and  vato[int(ii-1)][int(jj+1)]!=0 ):  
                                                                        # (x : -2 , y : 0)
                                                                        if ( 5>ii-2>-1   and 9>jj+2>-1 and vato[int(ii-2)][int(jj+2)]!=player_in_game
                                                                        and  vato[int(ii-2)][int(jj+2)]!=0 ):  
                                                                            vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x+2)]=0
                                                                            print(f"test vato [{piece_selected_elimin_y-2}][{piece_selected_elimin_x+2}] : {vato[piece_selected_elimin_y-2][piece_selected_elimin_x+2]}")
                                                                        vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x+1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y-1}][{piece_selected_elimin_x+1}] : {vato[piece_selected_elimin_y-1][piece_selected_elimin_x+1]}")
                                                                    # (x : 1 , y : -1)                                                                    
                                                                    if ( 5>ii+1>-1   and 9>jj-1>-1 and vato[int(ii+1)][int(jj-1)]!=player_in_game
                                                                    and  vato[int(ii+1)][int(jj-1)]!=0 ): 
                                                                        if ( 5>ii+2>-1   and 9>jj-2>-1 and vato[int(ii+2)][int(jj-2)]!=player_in_game
                                                                        and  vato[int(ii+2)][int(jj-2)]!=0 ): 
                                                                            vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x-2)]=0
                                                                            print(f"test vato [{piece_selected_elimin_y+2}][{piece_selected_elimin_x-2}] : {vato[piece_selected_elimin_y+2][piece_selected_elimin_x-2]}")
                                                                        vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x-1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y+1}][{piece_selected_elimin_x-1}] : {vato[piece_selected_elimin_y+1][piece_selected_elimin_x-1]}")
                                                                    
                                                                    # pygame.event.wait(1)
                                                                    vato[ii][jj]=0 
                                                                    print(f"elimin[{i-1}] : {elimin[i-1]}]")   
                                                                    print(f"x : {ii}, y : {jj}")
                                                                    print(f"test vato [{piece_selected_elimin_y}][{piece_selected_elimin_x}] : {vato[piece_selected_elimin_y][piece_selected_elimin_x]}")

                                                                jj-=1    
                                                            ii-=1
                                                        entre_elimin1=False
                                                        #deplacement pièces
                                                        if (int(chemin_clic_y),int(chemin_clic_x)) not in deplace:
                                                            deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                                            print(f"{(int(chemin_clic_y),int(chemin_clic_x))} deplace ajout : {deplace}")
                                                            # vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                            print(f"dernier select : {clic_farany_x},{clic_farany_y}")  
                                                            vato[piece_selectedY][piece_selectedX]=0                                                                                                                      
                                                            # x_pos_mat = piece_selectedX 
                                                            # y_pos_mat = piece_selectedY 
                                                            print(f"position piece select: {(y_pos_mat,x_pos_mat)}")
                                                            # (y_pos_mat,x_pos_mat)=(clic_farany_x,clic_farany_y)
                                                            elimin=[]
                                                            vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                        

                                            except:pass  

                                if elimin!=[] and ((difference_coordonne_y==-1 and difference_coordonne_x==1)):   
                                    # pygame.event.wait(1)
                                    for i in range(0,int(len(elimin)+1)):
                                        if i>0:
                                            try:                              
                                                cercle_y = ((elimin[i-1][0] *  100) + 100) 
                                                cercle_x = ((elimin[i-1][1] *  100) + 200)  
                                                pygame.event.wait(1)
                                                piece_elimin_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                                piece_elimine=pygame.draw.circle(screen, "red", (cercle_x  , cercle_y ), 35, 5)
                                                if piece_elimine.collidepoint(piece_elimin_position.x, piece_elimin_position.y) and pygame.mouse.get_pressed()[0] :        
                                                    pygame.event.wait(1)                                           
                                                    mouse_clic.x = ((piece_elimin_position.x - 150 ) // 100)
                                                    mouse_clic.y = ((piece_elimin_position.y - 50 ) // 100)
                                                    piece_selected_elimin_x=int(mouse_clic.x)
                                                    piece_selected_elimin_y=int(mouse_clic.y)

                                                    #elimine pièces 
                                                    entre_elimin1=True
                                                    while entre_elimin1:
                                                        ii=4
                                                        while ii>=0 :
                                                            jj=8
                                                            while jj>=0:
                                                                # if difference==(1,1):
                                                                if (ii,jj)==elimin[i-1]: 
                                                                    vato[piece_selected_elimin_y][piece_selected_elimin_x]=0 
                                                                    print(f"elimin[{i-1} : {elimin[i-1]}]")   
                                                                    print(f"x : {ii}, y : {jj}")
                                                                    print(f"test vato [{piece_selected_elimin_y}][{piece_selected_elimin_x}] : {vato[piece_selected_elimin_y][piece_selected_elimin_x]}")
                                                                    # (x : 1 , y : -1)
                                                                    if ( 5>ii-1>-1   and 9>jj+1>-1 and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x+1)]!=player_in_game
                                                                    and  vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x+1)]!=0):
                                                                    # and vato[int(piece_selected_elimin_y)][int(piece_selected_elimin_x)]!=player_in_game
                                                                    # and vato[int(piece_selected_elimin_y)][int(piece_selected_elimin_x)]!=0 ):                                                        
                                                                        #(x : -2 , y : -2)
                                                                        if ( 5>ii-2>-1   and 9>jj+2>-1 and vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x+2)]!=player_in_game 
                                                                        and vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x-2)]!=0 ):
                                                                        # and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=player_in_game
                                                                        # and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=0):                                                        
                                                                            vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x+2)]=0
                                                                            # vato[int(piece_selected_elimin_y-3)][int(piece_selected_elimin_x-3)]=0
                                                                            print(f"test vato [{piece_selected_elimin_y-2}][{piece_selected_elimin_x+2}] : {vato[piece_selected_elimin_y-2][piece_selected_elimin_x+2]}")
                                                                            # print(f"test vato [{piece_selected_elimin_y-3}][{piece_selected_elimin_x-3}] : {vato[piece_selected_elimin_y-3][piece_selected_elimin_x-3]}")
                                                                        
                                                                        vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x+1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y-1}][{piece_selected_elimin_x+1}] : {vato[piece_selected_elimin_y-1][piece_selected_elimin_x+1]}")
                                                                    
                                                                    if (5>ii+1>-1   and 9>jj-1>-1 and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x-1)]!=player_in_game 
                                                                    and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x-1)]!=0):   
                                                                        #(x : 2 , y : 2)
                                                                        if (5>ii+2>-1   and 9>jj-2>-1 
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x-2)]!=player_in_game
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x-2)]!=0):   
                                                                            print(f"test vato [{piece_selected_elimin_y+2}][{piece_selected_elimin_x-2}] : {vato[piece_selected_elimin_y+2][piece_selected_elimin_x-2]}")
                                                                            vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x-2)]=0                                                                        
                                                                        vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x-1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y+1}][{piece_selected_elimin_x-1}] : {vato[piece_selected_elimin_y+1][piece_selected_elimin_x+1]}")
                                                                        

                                                                jj-=1    
                                                            ii-=1
                                                        entre_elimin1=False
                                                        # moving=True
                                                        #deplacement pièces
                                                        if (int(chemin_clic_y),int(chemin_clic_x)) not in deplace:
                                                            deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                                            print(f"{(int(chemin_clic_y),int(chemin_clic_x))} deplace ajout : {deplace}")
                                                            vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                            vato[piece_selectedY][piece_selectedX]=0 
                                                            print(f"dernier select : {clic_farany_x},{clic_farany_y}")    
                                                                                                                   
                                                            # x_pos_mat = piece_selectedX 
                                                            # y_pos_mat = piece_selectedY 
                                                            print(f"position piece select: {(y_pos_mat,x_pos_mat)}")
                                                            (y_pos_mat,x_pos_mat)=(clic_farany_x,clic_farany_y)
                                                            elimin=[]

                                            except:pass     

                                if elimin!=[] and ((difference_coordonne_y==-1 and difference_coordonne_x==-1)):        
                                    for i in range(0,int(len(elimin)+1)):
                                        if i>0:
                                            try:                              
                                                # print(f"elimin_y[{i-1}][0] : {elimin[i-1][0]}")
                                                # print(f"elimin_x[{i-1}][1] : {elimin[i-1][1]}")
                                                cercle_y = ((elimin[i-1][0] *  100) + 100) 
                                                cercle_x = ((elimin[i-1][1] *  100) + 200)  
                                                # print(f"red y : {cercle_y}")
                                                # print(f"red x : {cercle_x}")
                                                # print(f"mouse pos : {pygame.mouse.get_pos()}")
                                                pygame.event.wait(1)
                                                piece_elimin_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                                piece_elimine=pygame.draw.circle(screen, "red", (cercle_x  , cercle_y ), 35, 5)
                                                if piece_elimine.collidepoint(piece_elimin_position.x, piece_elimin_position.y) and pygame.mouse.get_pressed()[0] :        
                                                    # pygame.event.wait(1)                                           
                                                    mouse_clic.x = ((piece_elimin_position.x - 150 ) // 100)
                                                    mouse_clic.y = ((piece_elimin_position.y - 50 ) // 100)
                                                    piece_selected_elimin_x=int(mouse_clic.x)
                                                    piece_selected_elimin_y=int(mouse_clic.y)

                                                    #elimine pièces 
                                                    entre_elimin1=True
                                                    while entre_elimin1:
                                                        ii=4
                                                        while ii>=0 :
                                                            jj=8
                                                            while jj>=0:
                                                                # if difference==(1,1):
                                                                if (ii,jj)==elimin[i-1]: 
                                                                    vato[piece_selected_elimin_y][piece_selected_elimin_x]=0 
                                                                    print(f"elimin[{i-1} : {elimin[i-1]}]")   
                                                                    print(f"x : {ii}, y : {jj}")
                                                                    print(f"test vato [{piece_selected_elimin_y}][{piece_selected_elimin_x}] : {vato[piece_selected_elimin_y][piece_selected_elimin_x]}")
                                                                    #(x : -1 , y : -1)
                                                                    if ( 5>ii-1>-1   and 9>jj-1>-1 and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=player_in_game
                                                                    and  vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=0
                                                                    and vato[int(piece_selected_elimin_y)][int(piece_selected_elimin_x)]!=player_in_game ):                                                        
                                                                        #(x : -2 , y : -2)
                                                                        if ( 5>ii-2>-1   and 9>jj-2>-1 and vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x-2)]!=player_in_game and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=player_in_game
                                                                        and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=0):                                                        
                                                                            vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x-2)]=0
                                                                            # vato[int(piece_selected_elimin_y-3)][int(piece_selected_elimin_x-3)]=0
                                                                            print(f"test vato [{piece_selected_elimin_y-2}][{piece_selected_elimin_x-2}] : {vato[piece_selected_elimin_y-2][piece_selected_elimin_x-2]}")
                                                                            # print(f"test vato [{piece_selected_elimin_y-3}][{piece_selected_elimin_x-3}] : {vato[piece_selected_elimin_y-3][piece_selected_elimin_x-3]}")
                                                                        
                                                                        vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y-1}][{piece_selected_elimin_x-1}] : {vato[piece_selected_elimin_y-1][piece_selected_elimin_x-1]}")
                                                                    
                                                                    if (5>ii+1>-1   and 9>jj+1>-1 and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]!=player_in_game 
                                                                    and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]!=0):   
                                                                        #(x : 2 , y : 2)
                                                                        if (5>ii+2>-1   and 9>jj+2>-1 
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]!=player_in_game
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]!=0):   
                                                                            print(f"test vato [{piece_selected_elimin_y+2}][{piece_selected_elimin_x+2}] : {vato[piece_selected_elimin_y+2][piece_selected_elimin_x+2]}")
                                                                            vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]=0                                                                        
                                                                        vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y+1}][{piece_selected_elimin_x+1}] : {vato[piece_selected_elimin_y+1][piece_selected_elimin_x+1]}")
                                                                        

                                                                jj-=1    
                                                            ii-=1
                                                        entre_elimin1=False
                                                        # moving=True
                                                        #deplacement pièces
                                                        if (int(chemin_clic_y),int(chemin_clic_x)) not in deplace:
                                                            deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                                            print(f"{(int(chemin_clic_y),int(chemin_clic_x))} deplace ajout : {deplace}")
                                                            vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                            vato[piece_selectedY][piece_selectedX]=0 
                                                            print(f"dernier select : {clic_farany_x},{clic_farany_y}")    
                                                                                                                   
                                                            # x_pos_mat = piece_selectedX 
                                                            # y_pos_mat = piece_selectedY 
                                                            print(f"position piece select: {(y_pos_mat,x_pos_mat)}")
                                                            (y_pos_mat,x_pos_mat)=(clic_farany_x,clic_farany_y)
                                                            elimin=[]

                                            except:pass     

                                if elimin!=[] and (difference_coordonne_y==1 and difference_coordonne_x==1):        
                                    for i in range(0,int(len(elimin)+1)):
                                        if i>0:
                                            try:                              
                                                # print(f"elimin_y[{i-1}][0] : {elimin[i-1][0]}")
                                                # print(f"elimin_x[{i-1}][1] : {elimin[i-1][1]}")
                                                cercle_y = ((elimin[i-1][0] *  100) + 100) 
                                                cercle_x = ((elimin[i-1][1] *  100) + 200)  
                                                # print(f"red y : {cercle_y}")
                                                # print(f"red x : {cercle_x}")
                                                # print(f"mouse pos : {pygame.mouse.get_pos()}")
                                                pygame.event.wait(1)
                                                piece_elimin_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                                piece_elimine=pygame.draw.circle(screen, "red", (cercle_x  , cercle_y ), 35, 5)
                                                if piece_elimine.collidepoint(piece_elimin_position.x, piece_elimin_position.y) and pygame.mouse.get_pressed()[0] :        
                                                    # pygame.event.wait(1)                                           
                                                    mouse_clic.x = ((piece_elimin_position.x - 150 ) // 100)
                                                    mouse_clic.y = ((piece_elimin_position.y - 50 ) // 100)
                                                    piece_selected_elimin_x=int(mouse_clic.x)
                                                    piece_selected_elimin_y=int(mouse_clic.y)

                                                    #elimine pièces 
                                                    entre_elimin1=True
                                                    while entre_elimin1:
                                                        ii=4
                                                        while ii>=0 :
                                                            jj=8
                                                            while jj>=0:
                                                                # if difference==(1,1):
                                                                if (ii,jj)==elimin[i-1]: 
                                                                    vato[piece_selected_elimin_y][piece_selected_elimin_x]=0 
                                                                    print(f"elimin[{i-1} : {elimin[i-1]}]")   
                                                                    print(f"x : {ii}, y : {jj}")
                                                                    print(f"test vato [{piece_selected_elimin_y}][{piece_selected_elimin_x}] : {vato[piece_selected_elimin_y][piece_selected_elimin_x]}")
                                                                    #(x : -1 , y : -1)
                                                                    if ( 5>ii-1>-1   and 9>jj-1>-1 and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=player_in_game
                                                                    and  vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=0
                                                                    and vato[int(piece_selected_elimin_y)][int(piece_selected_elimin_x)]!=player_in_game ):                                                        
                                                                        #(x : -2 , y : -2)
                                                                        if ( 5>ii-2>-1   and 9>jj-2>-1 and vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x-2)]!=player_in_game and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=player_in_game
                                                                        and vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]!=0):                                                        
                                                                            vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x-2)]=0
                                                                            # vato[int(piece_selected_elimin_y-3)][int(piece_selected_elimin_x-3)]=0
                                                                            print(f"test vato [{piece_selected_elimin_y-2}][{piece_selected_elimin_x-2}] : {vato[piece_selected_elimin_y-2][piece_selected_elimin_x-2]}")
                                                                            # print(f"test vato [{piece_selected_elimin_y-3}][{piece_selected_elimin_x-3}] : {vato[piece_selected_elimin_y-3][piece_selected_elimin_x-3]}")
                                                                        
                                                                        vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x-1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y-1}][{piece_selected_elimin_x-1}] : {vato[piece_selected_elimin_y-1][piece_selected_elimin_x-1]}")
                                                                    
                                                                    #(x : 1 , y : 1)
                                                                    if (5>ii+1>-1   and 9>jj+1>-1 and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]!=player_in_game 
                                                                    and vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]!=0):   
                                                                        #(x : 2 , y : 2)
                                                                        if (5>ii+2>-1   and 9>jj+2>-1 
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]!=player_in_game
                                                                        and vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]!=0):   
                                                                            print(f"test vato [{piece_selected_elimin_y+2}][{piece_selected_elimin_x+2}] : {vato[piece_selected_elimin_y+2][piece_selected_elimin_x+2]}")
                                                                            vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x+2)]=0                                                                        
                                                                        vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x+1)]=0
                                                                        print(f"test vato [{piece_selected_elimin_y+1}][{piece_selected_elimin_x+1}] : {vato[piece_selected_elimin_y+1][piece_selected_elimin_x+1]}")
                                                                        
                                                                jj-=1    
                                                            ii-=1
                                                        entre_elimin1=False
                                                        # moving=True
                                                        #deplacement pièces
                                                        if (int(chemin_clic_y),int(chemin_clic_x)) not in deplace:
                                                            deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                                            print(f"{(int(chemin_clic_y),int(chemin_clic_x))} deplace ajout : {deplace}")
                                                            vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                            vato[piece_selectedY][piece_selectedX]=0 
                                                            print(f"dernier select : {clic_farany_x},{clic_farany_y}")    
                                                                                                                   
                                                            # x_pos_mat = piece_selectedX 
                                                            # y_pos_mat = piece_selectedY 
                                                            print(f"position piece select: {(y_pos_mat,x_pos_mat)}")
                                                            (y_pos_mat,x_pos_mat)=(clic_farany_x,clic_farany_y)
                                                            elimin=[]

                                            except:pass     

                               
                                # if elimin!=[] and (difference_coordonne_y==1 and difference_coordonne_x==-1) :
                                # # or (difference_coordonne_y==1 and difference_coordonne_x==1)):        
                                #     for i in range(0,int(len(elimin)+1)):
                                #         if i>0:
                                #             try:                              
                                #                 cercle_y = ((elimin[i-1][0] *  100) + 100) 
                                #                 cercle_x = ((elimin[i-1][1] *  100) + 200)  
                                #                 pygame.event.wait(1)
                                #                 piece_elimin_position = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                #                 piece_elimine=pygame.draw.circle(screen, "red", (cercle_x  , cercle_y ), 35, 5)
                                #                 if piece_elimine.collidepoint(piece_elimin_position.x, piece_elimin_position.y) and pygame.mouse.get_pressed()[0] :        
                                #                     # pygame.event.wait(1)                                           
                                #                     mouse_clic.x = ((piece_elimin_position.x - 150 ) // 100)
                                #                     mouse_clic.y = ((piece_elimin_position.y - 50 ) // 100)
                                #                     piece_selected_elimin_x=int(mouse_clic.x)
                                #                     piece_selected_elimin_y=int(mouse_clic.y)

                                #                     #elimine pièces 
                                #                     entre_elimin1=True
                                #                     while entre_elimin1:
                                #                         ii=4
                                #                         while ii>=0 :
                                #                             jj=8
                                #                             while jj>=0:
                                #                                 # if difference==(-1,1):
                                #                                 if (ii,jj)==elimin[i-1]: 
                                #                                     # (x : -1 , y : 1)
                                #                                     if ( 5>ii-1>-1   and 9>jj+1>-1 and vato[int(ii-1)][int(jj+1)]!=player_in_game
                                #                                     and  vato[int(ii-1)][int(jj+1)]!=0 ):  
                                #                                         # (x : -2 , y : 0)
                                #                                         if ( 5>ii-2>-1   and 9>jj+2>-1 and vato[int(ii-2)][int(jj+2)]!=player_in_game
                                #                                         and  vato[int(ii-2)][int(jj+2)]!=0 ):  
                                #                                             vato[int(piece_selected_elimin_y-2)][int(piece_selected_elimin_x+2)]=0
                                #                                             print(f"test vato [{piece_selected_elimin_y-2}][{piece_selected_elimin_x+2}] : {vato[piece_selected_elimin_y-2][piece_selected_elimin_x+2]}")
                                #                                         vato[int(piece_selected_elimin_y-1)][int(piece_selected_elimin_x+1)]=0
                                #                                         print(f"test vato [{piece_selected_elimin_y-1}][{piece_selected_elimin_x+1}] : {vato[piece_selected_elimin_y-1][piece_selected_elimin_x+1]}")
                                #                                     # (x : 1 , y : -1)                                                                    
                                #                                     if ( 5>ii+1>-1   and 9>jj-1>-1 and vato[int(ii+1)][int(jj-1)]!=player_in_game
                                #                                     and  vato[int(ii+1)][int(jj-1)]!=0 ): 
                                #                                         if ( 5>ii+2>-1   and 9>jj-2>-1 and vato[int(ii+2)][int(jj-2)]!=player_in_game
                                #                                         and  vato[int(ii+2)][int(jj-2)]!=0 ): 
                                #                                             vato[int(piece_selected_elimin_y+2)][int(piece_selected_elimin_x-2)]=0
                                #                                             print(f"test vato [{piece_selected_elimin_y+2}][{piece_selected_elimin_x-2}] : {vato[piece_selected_elimin_y+2][piece_selected_elimin_x-2]}")
                                #                                         vato[int(piece_selected_elimin_y+1)][int(piece_selected_elimin_x-1)]=0
                                #                                         print(f"test vato [{piece_selected_elimin_y+1}][{piece_selected_elimin_x-1}] : {vato[piece_selected_elimin_y+1][piece_selected_elimin_x-1]}")
                                                                    
                                #                                     # pygame.event.wait(1)
                                #                                     vato[ii][jj]=0 
                                #                                     print(f"elimin[{i-1}] : {elimin[i-1]}]")   
                                #                                     print(f"x : {ii}, y : {jj}")
                                #                                     print(f"test vato [{piece_selected_elimin_y}][{piece_selected_elimin_x}] : {vato[piece_selected_elimin_y][piece_selected_elimin_x]}")

                                #                                 jj-=1    
                                #                             ii-=1
                                #                         entre_elimin1=False
                                #                         #deplacement pièces
                                #                         if (int(chemin_clic_y),int(chemin_clic_x)) not in deplace:
                                #                             deplace.append((int(chemin_clic_y),int(chemin_clic_x)))
                                #                             print(f"{(int(chemin_clic_y),int(chemin_clic_x))} deplace ajout : {deplace}")
                                #                             # vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                #                             print(f"dernier select : {clic_farany_x},{clic_farany_y}")  
                                #                             vato[piece_selectedY][piece_selectedX]=0                                                                                                                      
                                #                             # x_pos_mat = piece_selectedX 
                                #                             # y_pos_mat = piece_selectedY 
                                #                             print(f"position piece select: {(y_pos_mat,x_pos_mat)}")
                                #                             # (y_pos_mat,x_pos_mat)=(clic_farany_x,clic_farany_y)
                                #                             elimin=[]
                                #                             vato[int(chemin_clic_y)][int(chemin_clic_x)]=player_in_game
                                                        

                                #             except:pass  
                    
                    chemin_valide=[]
                    Chemin=[]
                    # elimin=[]

            

#vato
    v2=pygame.image.load("image/v1.PNG").convert_alpha()
#fixe taille vato (60,60)
    v2= pygame.transform.scale(v2, (60, 60))
    v1=pygame.image.load("image/v5 sans contour.PNG").convert_alpha()
    v1= pygame.transform.scale(v1, (60, 60))
#affiche vato
    initial_colonn=100-27
    initial_lign=200-31
    for enum_colonne,colonne in enumerate(vato):
        for enum_ligne,ligne in enumerate(colonne):                        
            if ligne== 1:
                screen.blit(v1, (initial_lign + 100*(enum_ligne),initial_colonn+(enum_colonne)*100))
            if ligne== 2:
                screen.blit(v2, (initial_lign+100*(enum_ligne),initial_colonn+(enum_colonne)*100))

#fps 60 img/s
    clock.tick(30)   

#MAJ   
    pygame.display.update()    
    
pygame.quit()






