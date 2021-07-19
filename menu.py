from time import sleep
import game


def menu_main():
    logo()

    opc = input('\n(1) Jogar\n(2) Créditos\n(3) Sair\n')
    if opc == '1':
        print('Carregando...\n')
        sleep(4)
        space()
        history()
        game.game_main()
    elif opc == '2':
        print('-=' * 20)
        credits()
        print('-=' * 20)
        sleep(5)
        space()
        menu_main()
    elif opc == '3':
        sleep(1)
        print('O Jogo foi encerrado!!')
    else:
        print('Valor Inválido!')
        space()
        menu_main()


def credits():
    print('Jogo criador por Mayke Erick.\nJogo com finalidade de aprendizagem.\n20/06/21')


def logo():
    print('\033[32m_____     _   _   __   _ ')
    print('|  _  \  | | | | |  \ | |')
    print('| |_| |  | | | | |   \| |')
    print('|  _  /  | | | | | |\   |')
    print('| | \ \  | |_| | | | \  |')
    print('|_|  \_\ \_____/ |_|  \_|')


def history():
    name = str(input('Digite seu nome: '))
    space()
    print(f'Olá, Meu nome é Carl.')
    sleep(2)
    print('Fiz essa carta com intuito de ajudar futuras pessoas que encontrarem meu abrigo antigo.')
    sleep(4)
    print('Devido as guerras mundiais o mundo está devastado e a humanidade irá entrar em extinção em breve.')
    sleep(4)
    print('Com isso, soube da existência de um grupo de sobreviventes à alguns quilômetros daqui.')
    sleep(4)
    print('A única forma de nós sobrevivermos é nós agrupando!!\n')
    sleep(4)
    print(f'Objetivo:\nGuiar {name} até o grupo.')


def space():
    print('\n' * 25)


def end():
    print('-=' * 15)
    print('Obrigado por jogar!')
    sleep(2)
    print('Jogo feito por\nestudante do 1° Período de Ciência da Computação.')
    print('-=' * 15)

if __name__ == '__main__':
    menu_main()

