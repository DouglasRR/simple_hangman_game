# Módulos
import random
from os import system, name

# Funções

def limpar_tela(): # Limpar terminal

    # Windows
    if name == "nt":
        _ = system("cls")
    
    # MAC ou LINUX
    else:
        _ = system("clear")

def game():

    limpar_tela()

    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de Palavras para o jogo
    palavras = ["banana", "uva", "abacate", "abacaxi", "maça"]

    # Escolhe aleatóriamente uma palavra na lista de palavras
    palavra = random.choice(palavras)

    # List Comprehension
    letras_descobertas = ["_" for letra in palavra]

    # Número de Chances
    chances = 6 

    # Lista de letras erradas
    letras_erradas = []

    # Enquanto o número de chances for maior que zero
    while chances > 0:
        # Mensagem
        print(" ".join(letras_descobertas))
        print("\nChances Restantes: ", chances)
        print("Letras Erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional de Finalização
        if "_" not in letras_descobertas:
            print("\n VOCÊ VENCEU! A palavra é: ", palavra)
            break

    # Condicional de Finalização
    if "_" in letras_descobertas:
        print("\n VOCÊ PERDEU! A palavra era: ", palavra)
# Bloco main
if __name__ == "__main__":
    game()
    print("Você finalizou o meu primeiro jogo! Obrigado e parabéns!")
    
