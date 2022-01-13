import pygame
import os
import random


pygame.font.init()

#Configs da janela
WIDTH, HEIGHT = 800, 800
janela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bala nas Estrelas")

#Carregar imagens
naveVermelha = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "nave_vermelha.png"))
naveAzul = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "nave_azul.png"))
naveAmarela = pygame.image.load(os.path.join("IntProg/Projeto/Imagens" , "nave_amarela.png"))
naveVerde = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "nave_verde.png"))
fundo = pygame.transform.scale(pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "fundo_preto.png")),(WIDTH,HEIGHT))
tiroAzul = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "tiro_azul.png"))
tiroVerde = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "tiro_verde.png"))
tiroAmarelo = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "tiro_amarelo.png"))
tiroVermelho = pygame.image.load(os.path.join("IntProg/Projeto/Imagens", "tiro_vermelho.png"))

#Classe mãe dos tipos de nave
class Nave:
    COOLDOWN = 20
    def __init__(self,x,y,vida=100):
        self.x = x
        self.y = y
        self.vida = vida
        self.nave_img = None
        self.laser_img = None
        self.lasers = []
        self.cd = 0

    def desenha(self,janela):
        janela.blit(self.nave_img, (self.x,self.y))
        for laser in self.lasers:
            laser.desenha(janela)

    def get_largura(self):
        return self.nave_img.get_width()
    
    def get_altura(self):
        return self.nave_img.get_height()

    def atira(self):
        if self.cd == 0:
            laser = Tiro(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cd = 1
    
    def move_tiro(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.movimento(vel)
            if laser.fora_tela(HEIGHT):
                self.lasers.remove(laser)
            elif laser.bateu(laser,obj):
                obj.vida -= 10
                self.lasers.remove(laser)


    def cooldown(self):
        if self.cd >= self.COOLDOWN:
            self.cd = 0
        elif self.cd > 0:
            self.cd += 1


#Classe da nave do jogador
class Jogador(Nave):

    def __init__(self, x, y, vida=100):
        super().__init__(x, y, vida=vida)
        self.nave_img = naveAmarela
        self.laser_img = tiroAmarelo
        self.mask = pygame.mask.from_surface(self.nave_img)
        self.vida_max = vida

    def move_tiro(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.movimento(vel)
            if laser.fora_tela(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.bateu(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
    


#Classe da nave dos inimigos
class Inimigo(Nave):
    MAPA_COR = {"vermelho": (naveVermelha,tiroVermelho), "verde": (naveVerde, tiroVerde), "azul": (naveAzul,tiroAzul)}
    def __init__(self, x, y, cor, vida=100):
        super().__init__(x, y, vida=vida)
        self.nave_img, self.laser_img = self.MAPA_COR[cor]
        self.mask = pygame.mask.from_surface(self.nave_img)

    def mover(self, velo):
        self.y += velo

#Classe dos tiros
class Tiro:
    def __init__(self, x, y, laserImg):
        self.x = x
        self.y = y
        self.laserImg = laserImg
        self.mask = pygame.mask.from_surface(self.laserImg)
    
    def desenha(self, janela):
        janela.blit(self.laserImg,(self.x,self.y))
    
    def movimento(self, velo):
        self.y += velo

    def fora_tela(self, height):
        return not(self.y <= height and self.y >= 0)

    def bateu (self, obj):
        return colisao(obj,self)

def colisao (obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None #caso o anterior n aconteça retorna None


def main():
    ligado = True
    perdeu = False
    FPS = 30
    nivel = 0
    vidas = 5
    escrita = pygame.font.SysFont("arial", 30)
    escrita_perdeu = pygame.font.SysFont("arial", 70)
    inimigos = []
    comprimento_onda = 5
    naveJogador = Jogador(300,650)
    naveJogador_velo = 7
    inimigos_velo = 1
    laser_velo = 5
    contador_perdeu = 0
    tempo = pygame.time.Clock()

    def atualizar_tela():
        janela.blit(fundo,(0,0))
        vidas_mostrar = escrita.render("Vidas: {a}".format(a = vidas), 1, (255,255,255))
        nivel_mostrar = escrita.render("Nivel: {a}".format(a = nivel), 1, (255,255,255))
        
        janela.blit(vidas_mostrar, (10,10))
        janela.blit(nivel_mostrar, (690,10))
        
        for inimigo in inimigos:
            inimigo.desenha(janela)
        
        naveJogador.desenha(janela)

        if perdeu:
            perdeu_texto = escrita_perdeu.render("VOCÊ PERDEU!",1 , (255,255,255)) 
            janela.blit(perdeu_texto,(WIDTH/2 - perdeu_texto.get_width()/2, 350))


        pygame.display.update()



    while ligado:
        tempo.tick(FPS)
        
        atualizar_tela()

        if vidas < 0 or naveJogador.vida <= 0:
            perdeu = True
            contador_perdeu += 1

        if perdeu:
            if contador_perdeu > FPS * 5:
                ligado = False
            else:
                continue

        if len(inimigos) == 0:
            nivel += 1
            comprimento_onda += 4
            for i in range(comprimento_onda):
                inimigo = Inimigo(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["vermelho", "azul", "verde"]))
                inimigos.append(inimigo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ligado = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and naveJogador.x - naveJogador_velo > 0:
            naveJogador.x -= naveJogador_velo
        if teclas[pygame.K_RIGHT] and naveJogador.x + naveJogador.get_largura() + naveJogador_velo < WIDTH:
            naveJogador.x += naveJogador_velo
        if teclas[pygame.K_DOWN] and naveJogador.y + naveJogador.get_altura() + naveJogador_velo < HEIGHT:
            naveJogador.y += naveJogador_velo
        if teclas[pygame.K_UP] and naveJogador.y - naveJogador_velo > 0:
            naveJogador.y -= naveJogador_velo
        if teclas[pygame.K_SPACE]:
            naveJogador.atira()

        for inimigo in inimigos[:]:
            inimigo.mover(inimigos_velo)
            inimigo.move_tiro(laser_velo, naveJogador)
            if inimigo.y + inimigo.get_altura()> HEIGHT:
                vidas -= 1
                inimigos.remove(inimigo)


        
        naveJogador.move_tiro(-laser_velo, inimigos)


main()

