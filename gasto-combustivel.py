# -*- coding: utf-8 -*-

if __name__ == "__main__":
    tempo_viagem = int(input())
    velocida_media = int(input())
    qtd = (velocida_media * tempo_viagem) / 12
    print("{0:.3f}".format(qtd))