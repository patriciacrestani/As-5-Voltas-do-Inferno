from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from Heroi import *
from Inimigo import *
from Tiro import *
from GameState import *
from VerticalFire import *
from Worm import *
from Demon import *
import random
from Fireball import *
random.seed()

#parametros inicias
janela = Window(900, 700)
fundo = GameImage("GameBG44.png")
w = fundo.width
h = fundo.height
fundo.set_position(0, 0)
janela.set_title("Zelda")
teclado = Window.get_keyboard()

#imagens
heroi = Heroi("PrincessZeldaFront.png", 417, 350)

hp = GameImage("ThreeHearts.png")
hp2 = GameImage("TwoHearts.png")
hp3 = GameImage("OneHeart.png")

hp3.set_position(-200,-200)
hp.set_position(197, 17)
hp2.set_position(-607,-607)

ponto = GameImage("Barra1.png")
ponto2 = GameImage("Barra2.png")
ponto3 = GameImage("Barra3.png")
ponto4 = GameImage("Barra4.png")
pontoRef = GameImage("Barra5.png")


ponto.set_position(-1000,-1000)
ponto2.set_position(-1500,-1500)
ponto3.set_position(-1700,-1700)
ponto4.set_position(-1300,-1300)
pontoRef.set_position(733,11)



#waveImagens
um = GameImage("1.png")
dois = GameImage("2.png")
tres = GameImage("3.png")
quatro = GameImage("4.png")
cinco = GameImage("5.png")
seis = GameImage("6.png")
sete = GameImage("7.png")


um.set_position(-500,-500)
dois.set_position(-500,-500)
tres.set_position(-500,-500)
quatro.set_position(-500,-500)
cinco.set_position(-500,-500)
seis.set_position(-500,-500)
sete.set_position(-500,-500)

onda = GameImage("trocaWave.png")
onda.set_position(0,590)



#arrays
inimigos = []
tiros = []
fireballs = []
vertical = []
worm = []
demon = []
#variaveis
qtdInimigos = 0
global VIDA, SCORE, clock, delay
delay = 0 
clock = 0
VIDA = 3
SCORE = 0
wave = 1

#estado inicial
gameState = GameState(GameState.ABERTURA)

def spawn_fireball(fireballs,w): #Atira Fireballs
    pos = random.randint(1,6)
    esquerda = [1,-1]
    direita = [2,-2]
    print(pos)
    if ( pos == 1):
        fireball = Fireball("BolaFogo.png",48,125, random.choice(esquerda))
        fireballs.append(fireball)
    elif(pos == 2):
        fireball = Fireball("BolaFogo.png",48,350, random.choice(esquerda))
        fireballs.append(fireball)
    elif(pos == 3):
        fireball = Fireball("BolaFogo.png",48,475, random.choice(esquerda))
        fireballs.append(fireball)
    elif(pos == 4):
        fireball = Fireball("BolaFogo.png",w - 48,475, random.choice(direita))
        fireballs.append(fireball)
    elif(pos == 5):
        fireball = Fireball("BolaFogo.png",w - 48,350, random.choice(direita))
        fireballs.append(fireball)
    elif(pos == 6):
        fireball = Fireball("BolaFogo.png",w - 48,125, random.choice(direita))
        fireballs.append(fireball)

def spawn_verticalBall(vertical): #Atira Fireballs
    pos = random.randint(1,4)
    
    print(pos)
    if ( pos == 1):
        fireball = VerticalFire("RedFire.png",225,10,1)
        vertical.append(fireball)
    elif(pos == 2):
        fireball = VerticalFire("RedFire.png",675,10, 1)
        vertical.append(fireball)
    elif(pos == 3):
        fireball = VerticalFire("RedFire.png",225,680,-1)
        vertical.append(fireball)
    elif(pos == 4):
        fireball = VerticalFire("RedFire.png",675,680, -1)
        vertical.append(fireball)

def spawn_worm(worm): #Gera worm
    pos = random.randint(1,6)
    
    print(pos)
    if ( pos == 1):
        fireball = Worm("wormLeft.png",10,125,1)
        worm.append(fireball)
    elif(pos == 2):
        fireball = Worm("wormLeft.png",10,350, 1)
        worm.append(fireball)
    elif(pos == 3):
        fireball = Worm("wormLeft.png",10,475, 1)
        worm.append(fireball)
    elif(pos == 4):
        fireball = Worm("wormRight.png",890,125, -1)
        worm.append(fireball)
    elif(pos == 5):
        fireball = Worm("wormRight.png",890,350, -1)
        worm.append(fireball)
    elif(pos == 6):
        fireball = Worm("wormRight.png",890,475, -1)
        worm.append(fireball)

def spawn_demon(demon): #Spawna Demons
    posX = random.randint(int(heroi.x - 80),int(heroi.x + 80))
    posY = random.randint(int(heroi.y - 80),int(heroi.y + 80))
    devil = Demon("demon.png",posX,posY)
    demon.append(devil)
    

def spawn_inimigo(inimigos, w, h): # Spawna Inimigos
    for i in range(16):
        if (i < 5):
            enemy = Inimigo("InimigoFront.png", random.uniform(48, w-48), h-115, random.uniform(-50, 50), random.uniform(-50, 50))
        elif (i < 10):
            enemy = Inimigo("InimigoBack.png", random.uniform(48, w-48), h-115, random.uniform(-50, 50), random.uniform(-50, 50))
        elif (i < 13):
            enemy = Inimigo("InimigoRight.png", 48, random.uniform(48, h-115), random.uniform(-50, 50), random.uniform(-50, 50))
        else:
            enemy = Inimigo("InimigoLeft.png", w-48, random.uniform(48, h-115), random.uniform(-50, 50), random.uniform(-50, 50))
        inimigos.append(enemy)

def spawn_tiros(tiros, x, y, posX, posY): # Spawna tiros
    bullet = Tiro("Tiro.png", x, y, posX, posY)
    tiros.append(bullet)

def morteInimigo(tiros, inimigos, qtdInimigos): # Mata o inimigo
    global SCORE
    for i in range(tiros.__len__()):
        for j in range(16):
            if (tiros[i].img.collided_perfect(inimigos[j].getImg())):
                inimigos.remove(inimigos[j])
                qtdInimigos -= 1
                tiros[i].visible = False
                SCORE += 50
                print(SCORE)

def resetWaveImg(): #Reseta as imagens que mostram a wave
    um.set_position(-500,-500)
    dois.set_position(-500,-500)
    tres.set_position(-500,-500)
    quatro.set_position(-500,-500)
    cinco.set_position(-500,-500)
    seis.set_position(-500,-500)
    sete.set_position(-500,-500)
    

def trocaWaveEffect(): #Efeito para marcar mudança de wave
        global waveEffect, ondaVisible
        waveSound = pygame.mixer.Sound("EvilLaugh.ogg")
        waveSound.set_volume(1)
        print(waveEffect)
        if (waveEffect % 2) == 0:
            
            waveSound.play(1,2000,1)
            ondaVisible = False
       

def resetScoreImg(): #Reseta as imagens da score
    ponto.set_position(-1000,-1000)
    ponto2.set_position(-1500,-1500)
    ponto3.set_position(-1700,-1700)
    ponto4.set_position(-1300,-1300)
    pontoRef.set_position(733,11)


ondaVisible = False
waveEffect = 0
# Tela de jogo
def jogando(teclado, qtdInimigos, tiros, inimigos, hp):
    #atributos iniciais
    
    hurt = pygame.mixer.Sound("Hurt.ogg")
    hurt.set_volume(1)
    shoot = pygame.mixer.Sound("Shoot.ogg")
    shoot.set_volume(1)
    
    
    
    global VIDA, SCORE, clock, delay,wave,ondaVisible, waveEffect
    clock += 1
    
    dt = janela.delta_time()
    #waves
    if wave >= 1:
        um.set_position(350,13);
        #wavesound()
        
    if wave >= 2:
        resetWaveImg()
        dois.set_position(350,13);
        #wavesound()

    if wave >= 3:
        resetWaveImg()
        tres.set_position(350,13);
        #wavesound()

    if wave >= 4:
        resetWaveImg()
        quatro.set_position(350,13);
        #wavesound()

    if wave >= 5:
        resetWaveImg()
        cinco.set_position(350,13);
        #wavessound()


    #Troca da Wave
    if SCORE >= 1000:
        
        wave += 1
        ondaVisible = True
        
        print(wave)
        SCORE = 0
        
    #Controladores
    if(VIDA <= 0):
        gameState.setState(GameState.GAME_OVER)
    if(wave > 5):
        gameState.setState(GameState.VITORIA)
    if(qtdInimigos != 16):
        spawn_inimigo(inimigos, w, h)
        qtdInimigos += 1

    if(clock % 70) == 0 and wave >= 4: #Atira Fireballs
        spawn_fireball(fireballs,w)
        shoot.play(1,1000,1)
        print(clock)
        print("Fire!")

    if(clock % 50) == 0 and wave >= 2: #Atira verticalBal
        spawn_verticalBall(vertical)
        #shoot.play(1,1000,1)
        print(clock)
        print("Vertical!")

    if(clock % 75) == 0 and wave >= 3: #Atira worm
        spawn_worm(worm)
        #shoot.play(1,1000,1)
        print(clock)
        print("Worm!")

    if(clock % 100) == 0 and wave >= 5: #Atira devil
        spawn_demon(demon)
        #shoot.play(1,1000,1)
        print(clock)
        print("Devil!")
        
    if(teclado.key_pressed("w")):  # Anda para cima
        heroi.y -= 3
        heroi.set_img("PrincessZeldaBack.png")
    if(teclado.key_pressed("s")):  # Anda para baixo
        heroi.y += 3
        heroi.set_img("PrincessZeldaFront.png")
    if(teclado.key_pressed("a")):  # Anda para esquerda
        heroi.x -= 3
        heroi.set_img("PrincessZeldaLeft.png")
    if(teclado.key_pressed("d")):  # Anda para direita
        heroi.x += 3
        heroi.set_img("PrincessZeldaRight.png")

        
    if(teclado.key_pressed("UP")):  # Atira para cima
        if(clock%30 == 0):
            spawn_tiros(tiros, heroi.x + 10, heroi.y, 0, -1)
          #  clock = 0
    if(teclado.key_pressed("DOWN")):  # Atira para baixo
        if(clock%30 == 0):
            spawn_tiros(tiros, heroi.x + 10, heroi.y + 48, 0, 1)
          #  clock = 0
    if(teclado.key_pressed("LEFT")):  # Atira para esquerda
        if(clock%30 == 0):
            spawn_tiros(tiros, heroi.x, heroi.y + 8, -1, 0)
          #  clock = 0
    if(teclado.key_pressed("RIGHT")):  # Atira para direita
        if(clock%30 == 0):
            spawn_tiros(tiros, heroi.x + 36, heroi.y + 8, 1, 0)
           # clock = 0


    if(teclado.key_pressed("ESC")):  # Fecha o programa
        janela.close()
   
    
    fundo.draw()
    heroi.draw()
    heroi.update(dt)
    hp.draw()
    hp2.draw()
    hp3.draw()
    pontoRef.draw()
    ponto.draw()
    ponto2.draw()
    ponto3.draw()
    ponto4.draw()
    if ondaVisible == True :
        #onda.draw()
        waveEffect += 1
        trocaWaveEffect()
    

    um.draw()
    dois.draw()
    tres.draw()
    
    heroi.windowCollision(48, 110, w-48, h-48)

    #Pontos

    if SCORE >= 0:
        resetScoreImg()

    if SCORE >= 200:
        resetScoreImg()
        ponto.set_position(733,11)
    if SCORE >= 400:
        resetScoreImg()
        ponto2.set_position(733,11)
    if SCORE >= 600:
        resetScoreImg()
        ponto3.set_position(733,11)
    if SCORE >= 800:
        resetScoreImg()
        ponto4.set_position(733,11)

    
    for i in range(0,len(fireballs)): # fireball
        fireballs[i].draw()
        fireballs[i].update()
        fireballs[i].windowCollision(48, 110, w-48, h-48)

    for i in range(0,len(worm)): # draw worm
        worm[i].draw()
        worm[i].update()
        worm[i].windowCollision(48, 110, w-48, h-48)

    for i in range(0,len(demon)): # draw demon
        
        demon[i].update()
        demon[i].draw()
        demon[i].windowCollision(48, 110, w-48, h-48)

    for i in range(0,len(vertical)): # vertical draw
        vertical[i].draw()
        vertical[i].update()
        vertical[i].windowCollision(0, 700, 0 , 900)

    for i in range(16): # Loop de inimigos
        inimigos[i].draw()
        inimigos[i].update(dt)
        inimigos[i].windowCollision(48, 110, w-48, h-48)

    for i in range(tiros.__len__()): # Loop de tiros
        tiros[i].draw()
        tiros[i].update(dt)
        tiros[i].windowCollision(48, 110, w-48, h-48)

    morteInimigo(tiros, inimigos, qtdInimigos)
    for j in range(16):  # Mata o heroi
        if (heroi.img.collided_perfect(inimigos[j].getImg())) and delay == 0:
            VIDA -= 1
            if(VIDA == 2):
                hp.set_position(-200, -200)
                
                hp2.set_position(197, 17)
                
            if (VIDA == 1):
                hp2.set_position(-400,-400)
                
                hp3.set_position(197, 17)
            
                

            #SCORE -= 20
            #delay player
            
            delay = 20
            for d in range(20):
                delay -= 1
            #HurtSound
            
            hurt.play(1,648,1)
                    
            #empurra player
            if (inimigos[j].x < heroi.x):
                heroi.x += 0.3*heroi.x
            elif ( inimigos[j].x > heroi.x):
                heroi.x -= 0.3*heroi.x

    for j in range(len(fireballs)):  # Mata o heroi com fireball
        if (heroi.img.collided_perfect(fireballs[j].getImg())) and delay == 0:
            VIDA -= 1
            if(VIDA == 2):
                hp.set_position(-200, -200)
                
                hp2.set_position(197, 17)
                
            if (VIDA == 1):
                hp2.set_position(-400,-400)
                
                hp3.set_position(197, 17)
            
                

            #SCORE -= 20
            #delay player
            
            delay = 30
            for d in range(30):
                delay -= 1
            #HurtSound
            
            hurt.play(1,648,1)
                   
            #empurra player
            if (fireballs[j].x < heroi.x):
                heroi.x += 0.3*heroi.x
            elif ( fireballs[j].x > heroi.x):
                heroi.x -= 0.3*heroi.x
    for j in range(len(vertical)):  # Mata o heroi com verticalball
        if (heroi.img.collided_perfect(vertical[j].getImg())) and delay == 0:
            VIDA -= 1
            if(VIDA == 2):
                hp.set_position(-200, -200)
                
                hp2.set_position(197, 17)
                
            if (VIDA == 1):
                hp2.set_position(-400,-400)
                
                hp3.set_position(197, 17)
            
                

            #SCORE -= 20
            #delay player
            
            delay = 30
            for d in range(30):
                delay -= 1
            #HurtSound
            
            hurt.play(1,648,1)
            vertical[j].x = -100
            vertical[j].y = -100
            #empurra player
            if (vertical[j].x < heroi.x):
                heroi.x += 0.3*heroi.x
            elif ( vertical[j].x > heroi.x):
                heroi.x -= 0.3*heroi.x

    for j in range(len(worm)):  # Mata o heroi com worm
        if (heroi.img.collided_perfect(worm[j].getImg())) and delay == 0:
            VIDA -= 1
            if(VIDA == 2):
                hp.set_position(-200, -200)
                
                hp2.set_position(197, 17)
                
            if (VIDA == 1):
                hp2.set_position(-400,-400)
                
                hp3.set_position(197, 17)
            
                

            #SCORE -= 20
            #delay player
            
            delay = 30
            for d in range(30):
                delay -= 1
            #HurtSound
            
            hurt.play(1,648,1)
            worm[j].x = -100
            worm[j].y = -100
            #empurra player
            if (worm[j].y < heroi.y):
                heroi.y += 0.3*heroi.y
            elif ( worm[j].y > heroi.y):
                heroi.y -= 0.3*heroi.y

    for j in range(len(demon)):  # Mata o heroi com demon
        if (heroi.img.collided_perfect(demon[j].getImg())) and delay == 0:
            VIDA -= 1
            if(VIDA == 2):
                hp.set_position(-200, -200)
                
                hp2.set_position(197, 17)
                
            if (VIDA == 1):
                hp2.set_position(-400,-400)
                
                hp3.set_position(197, 17)
            
                

            #SCORE -= 20
            #delay player
            
            delay = 30
            for d in range(30):
                delay -= 1
            #HurtSound
            
            hurt.play(1,648,1)
            '''      
            #empurra player
            if (worm[j].y < heroi.y):
                heroi.y += 0.3*heroi.y
            elif ( worm[j].y > heroi.y):
                heroi.y -= 0.3*heroi.y
            '''
# Tela de inicio
def abertura(teclado):
    
    fundo = GameImage("Start3.png")
    fundo.set_position(0, 0)
    fundo.draw()
    if(teclado.key_pressed("ENTER")):
        
        restart(qtdInimigos, tiros, inimigos, heroi, hp)
    if(teclado.key_pressed("ESC")):  # Fecha o programa
        janela.close()
    

# Tela pra restartar o jogo
def restart(qtdInimigos, tiros, inimigos, heroi, hp):
    heroi.x = 417
    heroi.y = 350
    del inimigos[:]
    del tiros[:]
    global VIDA, rep, SCORE, wave, ondaVisible, waveEffect
    ondaVisible = False
    resetWaveImg()
    um.set_position(500,20)
    waveEffect = 0
    wave = 1
    rep = 0 
    VIDA = 3
    hurt = pygame.mixer.Sound("Hurt.ogg")
    hp3.set_position(-200,-200)
    hp2.set_position(-300,-300)
    hp.set_position(197,17)

    ponto.set_position(-1200,-1200)
    ponto2.set_position(-1200,-1200)
    ponto3.set_position(-1200,-1200)
    ponto4.set_position(-1200,-1200)
    SCORE = 0
    
    fundo = GameImage("Restart.png")
    fundo.set_position(0, 0)
    fundo.draw()
    if(qtdInimigos == 0):
        print("Jogo restartado!")
    gameState.setState(GameState.JOGANDO)

#Tela de Game Over
def gameOver(teclado):
    
    
    fundo = GameImage("GameOver3.png")
    fundo.set_position(0, 0)
    fundo.draw()
    if(teclado.key_pressed("SPACE")):
        gameState.setState(GameState.RESTART)
    if(teclado.key_pressed("ESC")):  # Fecha o programa
        janela.close()

def vitoria(teclado):
    
    fundo = GameImage("Vitoria.png")
    fundo.set_position(0, 0)
    fundo.draw()
    if(teclado.key_pressed("SPACE")):
        gameState.setState(GameState.ABERTURA)
    if(teclado.key_pressed("ESC")):  # Fecha o programa
        janela.close()

#Controladores da musica
FaixaSendoTocada = 0
# 0 : nenhuma faixa ; 1 : faixa da abertura; 2 : faixa do jogo
#Protecao Contra Repeticao do GameOver : rep
rep = 0
# GameLoop
Win = pygame.mixer.Sound("Win.ogg")
while (True):
    if(gameState.getState() == GameState.ABERTURA):
        Win.stop()
        
        if FaixaSendoTocada == 0:
            FaixaSendoTocada = 1
            music = pygame.mixer.music.load("musicAbertura.ogg")
            pygame.mixer.music.play(-1)
        abertura(teclado)
    elif(gameState.getState() == GameState.JOGANDO):
        jogando(teclado, qtdInimigos, tiros, inimigos, hp)
        if FaixaSendoTocada == 1:
            pygame.mixer.music.fadeout(1000)
            FaixaSendoTocada = 2
            music = pygame.mixer.music.load("musicGameplay.ogg")
            pygame.mixer.music.play(-1)
    elif(gameState.getState() == GameState.RESTART):
        
        restart(qtdInimigos, tiros, inimigos, heroi, hp)
    elif(gameState.getState() == GameState.VITORIA):
        FaixaSendoTocada = 0
        pygame.mixer.music.stop()
        if rep == 0:
            rep = 1
            Win = pygame.mixer.Sound("Win.ogg")
            Win.set_volume(1)
            Win.play(-1,0,1)
        vitoria(teclado)
    else:
        
        if rep == 0:
            rep = 1
            GameOver = pygame.mixer.Sound("GameOver.ogg")
            GameOver.set_volume(1)
            GameOver.play(1,2000,1)
        gameOver(teclado)
    janela.update()
