import pygame,sys
from pygame.locals import*
from random import randint

#variables globales
ancho = 1000
alto = 650
color=pygame.Color(0,0,0)
color2=pygame.Color(250,0,0)
ventana =pygame.display.set_mode((ancho,alto))
listaConejo = []
tx = 0
tz = 0
vx=250
vy=250




# posicion de los yuyos para la salida del conejo
yuyo1 = (135,270)
yuyo2 = (235,420)
yuyo3 = (135,620)
yuyo4 = (435,320)#
yuyo5 = (435,620)#
yuyo6 = (535,470)#
yuyo7 = (835,370)
yuyo8 = (705,270)#
yuyo9 = (735,620)
yuyo10 = (935,520)
# limite global
limiteDerecha = 1100
limiteIzquierda = 100
limiteTop = 100
limiteDown = 580
#clase del jugador

#########################
#        PLAYER         #
#########################

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #imagenes derecha
        self.imagen_d1=pygame.image.load("imagenes/PJ con arma der/zanahoria_d1.png").convert_alpha()
        self.imagen_d2=pygame.image.load("imagenes/PJ con arma der/zanahoria_d2.png").convert_alpha()
        self.imagen_d3=pygame.image.load("imagenes/PJ con arma der/zanahoria_d3.png").convert_alpha()
        self.imagen_d4=pygame.image.load("imagenes/PJ con arma der/zanahoria_d4.png").convert_alpha()
        self.imagen_d5=pygame.image.load("imagenes/PJ con arma der/zanahoria_d5.png").convert_alpha()
        self.imagen_d6=pygame.image.load("imagenes/PJ con arma der/zanahoria_d6.png").convert_alpha()
        self.imagen_d7=pygame.image.load("imagenes/PJ con arma der/zanahoria_d7.png").convert_alpha()
        self.imagen_d8=pygame.image.load("imagenes/PJ con arma der/zanahoria_d8.png").convert_alpha()
        self.imagen_d9=pygame.image.load("imagenes/PJ con arma der/zanahoria_d9.png").convert_alpha()
        self.imagen_d10=pygame.image.load("imagenes/PJ con arma der/zanahoria_d10.png").convert_alpha()
        self.imagen_d11=pygame.image.load("imagenes/PJ con arma der/zanahoria_d11.png").convert_alpha()
        self.imagen_d12=pygame.image.load("imagenes/PJ con arma der/zanahoria_d12.png").convert_alpha()

        #imagenes izquierda
        self.imagen_i1=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i1.png").convert_alpha()
        self.imagen_i2=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i2.png").convert_alpha()
        self.imagen_i3=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i3.png").convert_alpha()
        self.imagen_i4=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i4.png").convert_alpha()
        self.imagen_i5=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i5.png").convert_alpha()
        self.imagen_i6=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i6.png").convert_alpha()
        self.imagen_i7=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i7.png").convert_alpha()
        self.imagen_i8=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i8.png").convert_alpha()
        self.imagen_i9=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i9.png").convert_alpha()
        self.imagen_i10=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i10.png").convert_alpha()
        self.imagen_i11=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i11.png").convert_alpha()
        self.imagen_i12=pygame.image.load("imagenes/PJ con arma izq/zanahoria_i12.png").convert_alpha()

        self.izquierda = False
        self.derecha = False
        self.arriba = False
        self.abajo = False
        self.correr = False
        self.cansado = False
        self.choca = False
        self.posXant = 0
        self.posYant = 0
        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen_d1,self.imagen_d2,self.imagen_d3,self.imagen_d4,self.imagen_d5,self.imagen_d6,self.imagen_d7,self.imagen_d8,self.imagen_d9,self.imagen_d10,self.imagen_d11,self.imagen_d12],
                       [self.imagen_i1,self.imagen_i2,self.imagen_i3,self.imagen_i4,self.imagen_i5,self.imagen_i6,self.imagen_i7,self.imagen_i8,self.imagen_i9,self.imagen_i10,self.imagen_i11,self.imagen_i12]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
       
        self.rect.top,self.rect.left=(71,33)
        self.rect.centerx,self.rect.centery=(ancho/2,alto/2)
        
        #variable par ver si se esta moviendo
        self.estamoviendo=False
        
        # 0 si va ala derecha 1 si va la izquierda
        self.orientacion=0

        #COLISIONANTE
        self.coli=pygame.image.load("imagenes/colisionante2.PNG")
        self.rectcoli=self.coli.get_rect()
        self.rectcoli.left=self.rect.left+70
        self.rectcoli.top=self.rect.top+145

        #CHOQUE1
        self.colcon=pygame.image.load("imagenes/colisionante3.PNG")
        self.rectcolcon=self.colcon.get_rect()
        self.rectcolcon.top=self.rect.top+145
        self.rectcolcon.left=self.rect.left+70
        
        #CHOQUE2
        self.colcon2=pygame.image.load("imagenes/colisionante3.PNG")
        self.rectcolcon2=self.colcon2.get_rect()
        self.rectcolcon2.top=self.rect.top+145
        self.rectcolcon2.left=self.rect.left+70
        
    def mover(self,vx,vy):

        if self.rect.left <=-20:
            self.rect.left = -20
        elif self.rect.right >1100:
            self.rect.right = 1100
        if self.rect.top <=100:
            self.rect.top = 100
        elif self.rect.bottom >=650:
            self.rect.bottom=650

        if self.choca == False:
            self.rect.move_ip(vx,vy)
            
        #if self.choca==True:
            
        #    self.rect.move_ip(self.posXant,self.posYant)
                
        #    self.choca=False
            
                 
       
    #funcion principal de actualizacion   
    def update(self,superficie,vx,vy,t):
        # si no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.nextimage()
            
        # mover el rectangulo    
        
        self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)

        #aca dibuja el rectangulo de colision con pasto para no avanzar, no tocar nada
        self.posicol=(self.rect.left+70,self.rect.top+145)
        #dibuja el rectangulo golpe izquierda
        self.posicol2=(self.rect.left+50,self.rect.top+163)
        #dibuja el rectangulo golpe derecha
        self.posicol3=(self.rect.left+110,self.rect.top+163)


        superficie.blit(self.coli,self.posicol)        
        superficie.blit(self.colcon,self.posicol2)
        superficie.blit(self.colcon2,self.posicol3)
        self.rectcoli=self.coli.get_rect()
        self.rectcoli.left=self.rect.left+70
        self.rectcoli.top=self.rect.top+145
        self.rectcolcon=self.colcon.get_rect()
        self.rectcolcon.top=self.rect.top+163
        self.rectcolcon.left=self.rect.left+50
        self.rectcolcon2=self.colcon2.get_rect()
        self.rectcolcon2.top=self.rect.top+163
        self.rectcolcon2.left=self.rect.left+110

        
        
    #funcion que se encarga de cambiar de imagen    
    def nextimage(self):
        self.imagen_actual= self.imagen_actual + 1
        
        if self.imagen_actual>((len(self.imagenes[0]) or (self.imagenes[1])) -1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0




        
#######################
#       ENEMIGO       #
#######################

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagen1 = pygame.image.load("imagenes/conejo_up/conejo0001.png").convert_alpha()
        self.imagen2 = pygame.image.load("imagenes/conejo_up/conejo0002.png").convert_alpha()
        self.imagen3 = pygame.image.load("imagenes/conejo_up/conejo0003.png").convert_alpha()
        self.imagen4 = pygame.image.load("imagenes/conejo_up/conejo0004.png").convert_alpha()
        self.imagen5 = pygame.image.load("imagenes/conejo_up/conejo0005.png").convert_alpha()
        self.imagen6 = pygame.image.load("imagenes/conejo_up/conejo0006.png").convert_alpha()
        self.imagen7 = pygame.image.load("imagenes/conejo_up/conejo0007.png").convert_alpha()
        self.imagen8 = pygame.image.load("imagenes/conejo_up/conejo0008.png").convert_alpha()

        self.tiempoBajada = 1  # variable usada como temporizador antes de q empieze bajar
        self.sube = True
        self.bajo = True
        self.espera = True
        self.imagenActual = 0
        self.listaImagenes = [self.imagen1,self.imagen2,self.imagen3,self.imagen4,self.imagen5,self.imagen6,self.imagen7,self.imagen8]
        self.imagenConejo = self.listaImagenes[self.imagenActual]
        self.rect = self.imagenConejo.get_rect()
        self.rect.top = posY
        self.rect.left = posX
        self.rect.centerx,self.rect.centery=(posX,posY)

        self.cone1=False
        self.cone2=False
        self.cone3=False
        self.cone4=False
        self.cone5=False
        self.cone6=False
        self.cone7=False
        self.cone8=False
        self.cone9=False
        self.cone10=False

        self.comprobarposic(posX,posY)

    def comprobarposic(self,posX,posY):
        if (posX,posY) == (135,270):
            self.cone1=True
            
        if (posX,posY) == (235,420):
            self.cone2=True
            
        if (posX,posY)==(135,620):
            self.cone3=True
            
        if (posX,posY)==(435,320):
            self.cone4=True
            
        if (posX,posY)==(435,620):
            self.cone5=True
            
        if (posX,posY)==(535,470):
            self.cone6=True
            
        if (posX,posY)==(835,370):
            self.cone7=True
            
        if (posX,posY)==(705,270):
            self.cone8=True
            
        if (posX,posY)==(735,620):
            self.cone9=True
            
        if (posX,posY)==(935,520):
            self.cone10=True

        
    def saleConejo(self,t):
        self.siguienteImagen()
        self.imagenConejo = self.listaImagenes[self.imagenActual]
        ventana.blit(self.imagenConejo,self.rect)
        
    def siguienteImagen(self):
        # cambia a la siguiente imagen mientras sube
        if self.sube == True and self.imagenActual < (len(self.listaImagenes)-1):
            self.imagenActual = self.imagenActual + 1
             # le descuento "Y" xq la imagen q sigue es mas grande necesita subir
            self.rect.top -= 10 
        else:
            self.sube = False  # convierte sube en falso para q no suba mas 
            self.baja()  # y va a a baja para comenzar a bajar
            
    def baja(self): 
            self.tiempoBajada += 1 # contador para q permanesca mas tiempo arriba

            if self.espera == True and self.tiempoBajada>40: # hace una pausa de 40 antes de comenzaar a bajar
                self.espera = False             # se acaba  la espera y  

            if self.espera == False:            # comienza a bajar
                    self.imagenActual = self.imagenActual - 1 #cuenta las imagenes para atras
                    self.rect.top += 10 #le sumo a "Y" xq ahora la imagen se va achicando
                    if self.imagenActual == 0: # cuando llego a 0
                        self.bajo = False #cambio la variable a falsa para poder eliminar el conejo 
                        
                        self.apagarposibilidaddegolpe()
                        

    def apagarposibilidaddegolpe(self):
        self.cone1=False
        self.cone2=False
        self.cone3=False
        self.cone4=False
        self.cone5=False
        self.cone6=False
        self.cone7=False
        self.cone8=False
        self.cone9=False
        self.cone10=False    
                

            
            
            
#############################
#          YUYOS            #
#############################

class Yuyo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagenYuyo = pygame.image.load("imagenes/conejo_up/yuyo1.png")
        self.recyuyo=self.imagenYuyo.get_rect()
        self.recyuyo.left=200
        self.recyuyo.top=200



    def dibujarYuyos(self,ventana):
        
        ventana.blit(self.imagenYuyo,(100,250)) 
        ventana.blit(self.imagenYuyo,(200,400))
        ventana.blit(self.imagenYuyo,(100,600))
        ventana.blit(self.imagenYuyo,(400,300))
        ventana.blit(self.imagenYuyo,(400,600))
        ventana.blit(self.imagenYuyo,(500,450))
        ventana.blit(self.imagenYuyo,(800,350))
        ventana.blit(self.imagenYuyo,(670,250))
        ventana.blit(self.imagenYuyo,(700,600))
        ventana.blit(self.imagenYuyo,(900,500))

#############################
#           SCORE           #
#############################
class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.imgscore= pygame.image.load("imagenes/conejito.png")
        self.imgrect=self.imgscore.get_rect()
        self.score=0
        self.fuente=pygame.font.Font('fonts/fuente.ttf',45)
        self.texto2=self.fuente.render("=",0,(238,252,48))
        
    def dibujarScore(self,ventana):
        ventana.blit(self.imgscore,(435,15))
        self.texto=self.fuente.render(str (self.score),1,(238,252,48))
        ventana.blit(self.texto,(520,45))
        ventana.blit(self.texto2,(500,45))

    def aumentarScore(self):
        self.score=self.score+1
        


#############################
#            PAUSA          #
#############################


    """def pausa(self):
      esperar = True
      while esperar:
        for evento in pygame.event.get():
         if evento.type == KEYDOWN:
              esperar = False"""


#############################
#     BARRA DE SPRINT       #
#############################
class Barra(pygame.sprite.Sprite):
    def __init__(self):
        self.colorRect=(100,255,100)
        self.valorx=306
               
        #Imagenes de la barra
        self.barra1=pygame.image.load("imagenes/conejo_up/Barra105.PNG").convert_alpha()
    ####VERIFICACION DE COLORES###########################

        #La Dibujo
    def dibujarBarra(self,ventana):
        ventana.blit(self.barra1,(15,15))

    def restarBarra(self):
        self.valorx-=5
        self.dibujarRectangulo()

    def sumarBarra(self):
        self.valorx+=3
        self.dibujarRectangulo()
        
    def dibujarRectangulo(self):
        self.Rectangulo=pygame.draw.rect(ventana,self.colorRect,(20,20,self.valorx,26))
        if self.valorx >= 304:
            self.valorx = 304
        if self.valorx <= 4:
            self.valorx = 4
    #COMPROBAR COLORES PARA BARRA
        if self.valorx >200:
            self.colorRect=(100,255,100)
        if self.valorx <=200 and self.valorx >=175:
            self.colorRect=(175,250,100)
        if self.valorx <= 175 and self.valorx >= 150:
            self.colorRect=(225,250,100)
        if self.valorx <= 150 and self.valorx >= 125:
            self.colorRect=(250,250,100)
        if self.valorx <= 125 and self.valorx >= 100:
            self.colorRect=(250,230,75)
        if self.valorx <= 100 and self.valorx >= 75:
            self.colorRect=(255,210,60)
        if self.valorx <= 75 and self.valorx >= 50:
            self.colorRect=(255,150,40)
        if self.valorx <= 50 and self.valorx >= 30:
            self.colorRect=(255,110,60)
        if self.valorx <= 30 and self.valorx >= 10:
            self.colorRect=(255,50,2)
        if self.valorx < 10:
            self.colorRect=(255,0,0)
                      
        
    
########################################################################



def probConejo():
        
        global tz  ##aca esta el secreto, invoco a las 2 varialbes q tengo como globales
        global tx  ## entonces actuan como si fueran locales dentro de la funcion y toman los valores q les de y se quedan con
                   ##cuando vuelva aca las varialbes seguiran teninendo los mismo valores
    ## esta comparacion es para q no salga el conejo 2 veces del mismo lugar
        while tx == tz:
            tx = randint(1,10)
        tz = tx
        if tx == 1:
            posX,posY = yuyo1
        elif tx == 2:
            posX,posY = yuyo2
        elif tx == 3:
            posX,posY = yuyo3
        elif tx == 4:
            posX,posY = yuyo4
        elif tx == 5:
            posX,posY = yuyo5
        elif tx == 6:
            posX,posY = yuyo6
        elif tx == 7:
            posX,posY = yuyo7
        elif tx == 8:
            posX,posY = yuyo8
        elif tx == 9:
            posX,posY = yuyo9
        elif tx == 10:
            posX,posY = yuyo10
            
        conejo= Enemigo(posX,posY) # creo el conejo, en la pocicion q salio
        listaConejo.append(conejo) # lo agrego a la lista de conejos
        



################################################################################
################################################################################
        ###############################################################


def main():
    pygame.init()
###########MUSICAAAAAAAAAA
#    pygame.mixer.music.load("sonidos/LoLArcade.mp3")
#    pygame.mixer.music.play()
#    pygame.mixer.music.set_volume(0.3)
############################

    
    
    fondo = pygame.image.load("imagenes/fondo1.png")
    pantalla = ventana
    salir=False
    reloj1= pygame.time.Clock()
    #creo un player
    player1=Player()
    
    golpe=False
    vx,vy=0,0
    velocidad=7
    
    #auxiliares para el movimiento
    yuyos=Yuyo()
    cansado = False
    t=1
    tiempoProbabilidad=0
    score=Score()
    
    objBarra=Barra()
    objBarra.dibujarRectangulo()
    while salir!=True:#LOOP PRINCIPAL
        score.dibujarScore(ventana)
        ventana.blit(fondo,(0,0))
        score.dibujarScore(ventana)
        objBarra.dibujarBarra(ventana)
        objBarra.dibujarRectangulo()


################################################################################
        ################################################
        # COLISIONES AUXILIARES #

        
        
        

        #COLISIONES PARA NO CAMINAR POR EL PASTO
        pygame.draw.rect(ventana,color,player1.rectcolcon)
        pygame.draw.rect(ventana,color,(112,250,45,30)) #RectanguloAuxYUYO1 BORRAR DESPUES
        if player1.rectcoli.colliderect(112,250,45,30):
            print "hola"
           #player1.choca=True
    
        pygame.draw.rect(ventana,color,(210,400,50,27)) #2
        if player1.rectcoli.colliderect(210,400,50,27):
            print "auch"
            
        pygame.draw.rect(ventana,color,(115,605,45,30))#3
        if player1.rectcoli.colliderect(115,605,45,30):
            print "auch"
        
        pygame.draw.rect(ventana,color,(415,303,45,30))
        if player1.rectcoli.colliderect(415,303,45,30):
            print "auch"

        pygame.draw.rect(ventana,color,(415,603,45,30))#5
        if player1.rectcoli.colliderect(415,603,45,30):
            print "auch"

        pygame.draw.rect(ventana,color,(512,452,45,30))
        if player1.rectcoli.colliderect(512,452,45,30):
            print "auch"

        pygame.draw.rect(ventana,color,(815,350,45,30))
        if player1.rectcoli.colliderect(815,350,45,30):#7
            print "auch"

        pygame.draw.rect(ventana,color,(690,255,47,25))
        if player1.rectcoli.colliderect(690,255,47,25):
            print "auch"

        pygame.draw.rect(ventana,color,(710,600,47,25))
        if player1.rectcoli.colliderect(710,600,47,25):#9
            print "auch"

        pygame.draw.rect(ventana,color,(910,500,47,25))
        if player1.rectcoli.colliderect(910,500,47,25):
            print "auch"

####################################################################################################################
        #COLISIONES PUNTERIA DERECHA
        punteria = False
        if player1.rectcolcon.colliderect(112,250,45,30):
            punteria=True
            if punteria == True and golpe==True and player1.orientacion==1 and conejo.cone1==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                #ACA VA EL CAMBIO DE IMAGENES POR UN GOLPE
                conejo.cone1=False

        if player1.rectcolcon.colliderect(210,400,50,27):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone2==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone2=False
        if player1.rectcolcon.colliderect(115,605,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone3==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone3=False
        if player1.rectcolcon.colliderect(415,303,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone4==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone4=False
        if player1.rectcolcon.colliderect(415,603,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone5==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone5=False
        if player1.rectcolcon.colliderect(512,452,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone6==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone6=False
        if player1.rectcolcon.colliderect(815,350,45,30):
            punteri=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone7==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone7=False
        if player1.rectcolcon.colliderect(690,255,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone8==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone8=False
        if player1.rectcolcon.colliderect(710,600,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone9==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone9=False
        if player1.rectcolcon.colliderect(910,500,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==1 and conejo.cone10==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone10=False
###################################################################################################################
        #COLISIONES PUNTERIA IZQUIERDA

        if player1.rectcolcon2.colliderect(112,250,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone1==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone1=False
        if player1.rectcolcon2.colliderect(210,400,50,27):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone2==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone2=False
        if player1.rectcolcon2.colliderect(115,605,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone3==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone3=False
        if player1.rectcolcon2.colliderect(415,303,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone4==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone4=False
        if player1.rectcolcon2.colliderect(415,603,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone5==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone5=False
        if player1.rectcolcon2.colliderect(512,452,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone6==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone6=False
        if player1.rectcolcon2.colliderect(815,350,45,30):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone7==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone7=False
        if player1.rectcolcon2.colliderect(690,255,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone8==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone8=False
        if player1.rectcolcon2.colliderect(710,600,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone9==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone9=False
        if player1.rectcolcon2.colliderect(910,500,47,25):
            punteria=True
            if punteria == True and golpe == True and player1.orientacion==0 and conejo.cone10==True:
                print "GOLPE ACERTADO"
                score.aumentarScore()
                conejo.cone10=False

##############################################################################################################################
                
        for event in pygame.event.get():
            #control de eventos
            if event.type == pygame.QUIT:
                salir=True
            ###PAUSA###
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    
                  esperar = True
                  player1.izquierda=False
                  player1.derecha=False
                  player1.arriba=False
                  player1.abajo=False
                  player1.correr = False
                  vx=0
                  vy=0
                  pausado = True
                  if pausado:
                     ventana2 =pygame.display.set_mode((1000,650))
                     pausa=pygame.image.load("Imagenes/enPausa.jpg")
                     ventana2.blit(pausa,(0,0))
                     pygame.display.update()
                  while esperar:
                    """if pausado:
                       pausa=pygame.image.load("Imagenes/sl.jpg")
                       ventana.blit(pausa,(0,0))"""
                    for event in pygame.event.get():
                          if event.type == pygame.KEYDOWN:
                              if event.key==pygame.K_p:
                                  esperar = False
                                  pausado = False
                          if event.type == pygame.QUIT:
                              pygame.quit()
                              sys.exit()





                if event.key == pygame.K_s:
                    player1.correr = True
                    print "corre"
                if event.key == pygame.K_SPACE:
                    golpe=True
                    
                if event.key == pygame.K_LEFT:
                    player1.izquierda =True
                if event.key == pygame.K_RIGHT:
                    player1.derecha=True
                if event.key== pygame.K_UP:
                    player1.arriba=True
                if event.key == pygame.K_DOWN:
                    player1.abajo =True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    golpe=False
                if event.key == pygame.K_s:
                    player1.correr =False
                if event.key == pygame.K_LEFT:
                    player1.izquierda =False
                    if player1.derecha:
                        vx=velocidad
                    else:
                        vx=0
                if event.key == pygame.K_RIGHT:
                    player1.derecha=False
                    if player1.izquierda:vx=-velocidad
                    else:vx=0
                if event.key== pygame.K_UP:
                    player1.arriba=False
                    if player1.abajo:vy=velocidad
                    else:vy=-0
                if event.key == pygame.K_DOWN:
                    player1.abajo=False
                    if player1.arriba:
                        vy=-velocidad
                        
                    else:vy=0
                   
        if player1.correr ==True:
            objBarra.restarBarra()
            if objBarra.valorx <= 10:
                cansado = True    
        if player1.correr ==False:
            objBarra.sumarBarra()
            if objBarra.valorx > 10:
                cansado = False 
#Boton Izquierda
        if player1.izquierda == True:
            if player1.correr == True:
                if cansado == True:
                    velocidad = 7
                if cansado == False:
                    velocidad = 15
            else: velocidad = 7
            vx = - velocidad
            
#Boton derecha
        elif player1.derecha == True:
            if player1.correr == True:
                if cansado == True:
                    velocidad = 7
                if cansado == False:
                    velocidad = 15
            else: velocidad = 7
            vx = + velocidad
            
#BOTON ARRIBA
        if player1.arriba == True:
            if player1.correr == True:
                if cansado == True:
                    velocidad = 7
                if cansado == False:
                    velocidad = 15
            else: velocidad = 7
            vy = - velocidad
            
#BOTON ABAJO
        elif player1.abajo == True:
            if player1.correr == True:
                if cansado == True:
                    velocidad = 7
                if cansado == False:
                    velocidad = 15
            else: velocidad = 7
            
            vy = +velocidad
            
        reloj1.tick(30)# 25 fps
        
        #auxiliar de la animacion, retrasa el cambio de imagen
        tiempoProbabilidad += 1  
        if tiempoProbabilidad>50:
            tiempoProbabilidad=0
            
        
        # actualizar jugador
        # si es momento de sacar un conjeo llamo a probConejo
        if tiempoProbabilidad == 5: # este tiempo probabilidad es 
            
            probConejo()           # para q no salgan conejos a patadas
            
        if len(listaConejo) > 0:    #aca recorre la lista de conejos
            for conejo in listaConejo: #por cada conejo invoca a sale.conejo
                conejo.saleConejo(t)
                if conejo.bajo == False: #aca si el atributo .bajo es False es xq
                    listaConejo.remove(conejo)#el conejo bajo y hay q eliminar el
                    


                    
         

        #actualizar pantalla
        yuyos.dibujarYuyos(ventana)
        player1.update(pantalla,vx,vy,t)
        pygame.display.update()
        score.dibujarScore(ventana)     
    pygame.quit()
cansado=False
main()
