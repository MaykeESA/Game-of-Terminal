import enemy
import inventory
from random import randrange
from menu import space
from menu import end
from time import sleep



def game_main():
    print('\033[32m-=' * 13 + '-')
    print('        Caminhos ')

    print('-=' * 13 + '-')
    print('|           (1)           |')
    print('|          Norte          |')
    print('| (4) Oeste  +  Leste (3) |')
    print('|           Sul           |')
    print('|           (2)           |')
    print('-=' * 13 + '-')
    choice()
    end()


def choice():
    while True:
        c1 = input('Escolha um caminho: ').strip()
        space()
        if c1 == '1':
            norte_1()
            break
        elif c1 == '2':
            sul_4()
            break
        elif c1 == '3':
            print('Você segue pela floresta até encontrar uma cabana.')
            sleep(1)
        elif c1 == '4':
            print('Você continua caminhando...')
            sleep(1)
            print('Até que você se depara com um ZUMBI!')
            break
        else:
            print('Valor Inválido!!')
            choice()
        break


def norte_1():
    print('Você segue pelo Norte!')
    sleep(1)
    print('Você avistou uma casa e algo no fim da estrada! ')
    sleep(1)
    cn1 = input('(1) Casa / (2) Estrada: ')
    space()
    if cn1 == '1':
        print('Você entra na casa e se depara com uma pessoa...')
        sleep(2)
        print('Ela parece morta por dentro, você se aproxima dela tentando chamar sua atenção')
        sleep(3)
        print('Em determinado ponto ela se aproxima muito rápido em sua direção!\n')
        sleep(2)
        norte_casa_1()
    elif cn1 == '2':
        print('Você continua andando pela estrada até que encontra um báu')
    else:
        print('Valor Inválido!!')
        norte_1()


def norte_casa_1():
    c1 = input('(1) Atacar / (2) Inventário: ')
    if c1 == '1':
        if sum(inventory.facaList) == 1:
            while enemy.vida_zumbi() <= 0:
                dano_faca = randrange(2, 5)
                vida_zumbi_faca = dano_faca - enemy.vida_zumbi()
                print(f'Você ataca com a Faca e da um total de {dano_faca} dano no inimigo!\nO inimigo fica com {vida_zumbi_faca} de vida')

        elif len(inventory.shotgunList) == 1:
            while enemy.vida_zumbi() <= 0:
                dano_shot = randrange(4, 10)
                vida_zumbi_shotgun = dano_shot - enemy.vida_zumbi()
                print(f'Você ataca com a Faca e da um total de {dano_shot} dano no inimigo!\nO inimigo fica com {vida_zumbi_shotgun} de vida')

        elif len(inventory.pistolList) == 1:
            while enemy.vida_zumbi() <= 0:
                dano_pistol = randrange(3, 7)
                vida_zumbi_pistol = dano_pistol - enemy.vida_zumbi()
                print(f'Você ataca com a Faca e da um total de {dano_pistol} dano no inimigo!\nO inimigo fica com {vida_zumbi_pistol} de vida')
        else:
            print('Você não tem nada equipado!')
        norte_casa_1()

    elif c1 == '2':
        inventory.inventory_main()
    else:
        print('Valor Inválido!a')
        space()
        norte_casa_1()



def sul_4():
    print('Você segue o caminho do Sul, até que ...')
    sleep(2)
    print('até que...')
    sleep(2)
    print('até que..')
    sleep(2)
    print('até que.')
    sleep(1)
    print('Você tropeça em um galho e cai de cabeça em uma pedra bem afiada!')
    print('Você morreu!')


if __name__ == '__main__':
    game_main()
