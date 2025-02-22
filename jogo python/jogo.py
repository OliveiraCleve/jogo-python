import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)
laranja = (255, 165, 0)

# Definir tamanho da janela
largura_janela = 600
altura_janela = 400
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobrinha com Obstáculos e Fases')

# Configurar o relógio do jogo
clock = pygame.time.Clock()
velocidade_inicial = 10

# Definir tamanho da cobra e velocidade
tamanho_cobra = 10

# Definir fonte do texto
fonte = pygame.font.SysFont(None, 35)

# Função para exibir mensagem
def mostrar_mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura_janela / 6, altura_janela / 3])

# Função para mostrar pontuação e nível
def mostrar_pontuacao(pontos, nivel):
    valor_pontos = fonte.render("Pontuação: " + str(pontos), True, branco)
    valor_nivel = fonte.render("Nível: " + str(nivel), True, branco)
    tela.blit(valor_pontos, [0, 0])
    tela.blit(valor_nivel, [0, 30])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False
    nivel = 1
    pontos = 0

    x1 = largura_janela / 2
    y1 = altura_janela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 10.0) * 10.0

    obstaculos = []
    for _ in range(nivel):
        obstaculo_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 10.0) * 10.0
        obstaculo_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 10.0) * 10.0
        obstaculos.append([obstaculo_x, obstaculo_y])

    velocidade_cobra = velocidade_inicial + (nivel - 1) * 2

    while not game_over:

        while game_close:
            tela.fill(preto)
            mostrar_mensagem("Você perdeu! Pressione Q-Quitar ou C-Continuar", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -tamanho_cobra
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_cobra
                    x1_mudanca = 0

        if x1 >= largura_janela or x1 < 0 or y1 >= altura_janela or y1 < 0:
            game_close = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        
        for obstaculo in obstaculos:
            pygame.draw.rect(tela, laranja, [obstaculo[0], obstaculo[1], tamanho_cobra, tamanho_cobra])

        cobra_cabeca = [x1, y1]
        cobra.append(cobra_cabeca)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for x in cobra[:-1]:
            if x == cobra_cabeca:
                game_close = True

        for obstaculo in obstaculos:
            if x1 == obstaculo[0] and y1 == obstaculo[1]:
                game_close = True

        desenhar_cobra(tamanho_cobra, cobra)
        mostrar_pontuacao(pontos, nivel)
        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1
            pontos += 10

            if pontos % 50 == 0:
                nivel += 1
                velocidade_cobra += 2
                obstaculo_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 10.0) * 10.0
                obstaculo_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 10.0) * 10.0
                obstaculos.append([obstaculo_x, obstaculo_y])

        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

# Função para desenhar a cobra
def desenhar_cobra(tamanho_cobra, cobra):
    for x in cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], tamanho_cobra, tamanho_cobra])

# Iniciar o jogo
jogo()

