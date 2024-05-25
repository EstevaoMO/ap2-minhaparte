import time

from . import som
from . import mecanicas
from .inputbox import ler_texto
from .buttonbox import escolher_classe

from ..gui.tela import Tela

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank



""" tem que importar """
from ..mecanicas.dificuldade import Dificuldade





from ..personagens.tesouro import Tesouro
from ..personagens.npc import NPC
from ..personagens.inimigos.boss import Boss

import pygame







""" atribuir variável """

dificuldade = Dificuldade()





def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def executar():
    som.iniciar_musica()

    nome = ler_texto()
    classe = escolher_classe()
    match classe:
        case "Guerreiro":
            aventureiro = Guerreiro(nome)
        case "Tank":
            aventureiro = Tank(nome)
        case _:
            aventureiro = Aventureiro(nome)

    tesouro = Tesouro()
    
    npc = NPC(tesouro)
    tela = Tela()

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

                if teclas[pygame.K_c]:
                    aventureiro.trocar_char()
                elif teclas[pygame.K_v]:
                    aventureiro.trocar_cor()
                elif teclas[pygame.K_b]:
                    aventureiro.trocar_cor(aleatorio=True)






                """ ler eventos """
                if teclas[pygame.K_m]:
                    dificuldade.indice *= 1.1
                elif teclas[pygame.K_n]:
                    dificuldade.indice /= 1.1








                
                if teclas[pygame.K_SPACE]:
                    mecanicas.conversar(aventureiro, npc)
                else:
                    direcao = determinar_direcao(teclas)





                    """ difciuldade.indice entrou no movimentar """
                    if direcao != "" and not mecanicas.movimentar(aventureiro, direcao, npc, dificuldade.indice):
                        jogo_rodando = False

                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss()




                        """ o boss tbm é alterado """
                        boss.forca *= dificuldade.indice
                        boss.vida *= dificuldade.indice
                        boss.defesa *= dificuldade.indice
                        
                        
                        
                        
                        if mecanicas.iniciar_combate(aventureiro, boss):
                            aventureiro.status = f"Parabéns! Você derrotou {boss.nome} e encontrou o tesouro!"
                        else:
                            aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                        jogo_rodando = False

        # Renderização na tela



        """ renderiza com dificuldade """
        tela.renderizar(aventureiro, tesouro, npc, dificuldade)
        pygame.time.Clock().tick(60)

    time.sleep(2)
