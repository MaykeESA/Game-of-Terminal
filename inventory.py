import game


inventoryList = ['Curativo', 'Vazio', 'Vazio', 'Faca']
shotgunList = []
pistolList = []
facaList = []
vida = 10


def inventory_main():
    print('\033[32m-=' * 25)
    print(f'O invetário possúi a capacidade máxima de {len(inventoryList)} itens\nItens: ')
    print(' | '.join(inventoryList))
    print('-=' * 25)
    equip_inventory(vida)
    return_main()


def equip_inventory(vida):
    while True:
        try:
            if 'Curativo' in inventoryList:
                op1 = input('Deseja utilizar o Curativo? (S/N) ').strip().upper()
                if op1 == 'S':
                    vida += 3
                    inventoryList.remove('Curativo')
                    inventoryList.append('Vazio')
                    print(f'Você foi curado, possúi {vida} vida(s)!')
                elif op1 == 'N':
                    print('Você não se curou!!')
                else:
                    raise ValueError

            if 'Shotgun' in inventoryList:
                op2 = input('Deseja equipar a Shotgun? (S/N) ').strip().upper()
                if op2 == 'S':
                    if len(shotgunList) == 1:
                        print('A shotgun já está equipada!!')
                        break
                    shotgunList.append(1)
                    print('Você equipou a Shotgun!!')
                elif op2 == 'N':
                    print('Você não equipou a Shotgun!!')
                else:
                    raise AttributeError

            if 'Pistola' in inventoryList:
                op3 = input('Deseja equipar a Pistola? (S/N) ').strip().upper()
                if op3 == 'S':
                    if len(pistolList) == 1:
                        print('A Pistola já está equipada!!')
                        break
                    pistolList.append(1)
                    print('Você equipou a Shotgun!')
                elif op3 == 'N':
                    print('Você não equipou a Pistola!!')
                else:
                    raise ZeroDivisionError

            if 'Faca' in inventoryList:
                op4 = input('Deseja equipar a Faca? (S/N)\n').strip().upper()
                if op4 == 'S':
                    if len(facaList) == 1:
                        print('A Faca já está equipada!!')
                        break
                    facaList.append(1)
                    print('Você equipou a Faca!')
                elif op4 == 'N':
                    print('Você não equipou a Faca!!')
                else:
                    raise BufferError

        except BufferError or ZeroDivisionError or AttributeError or ValueError:
            print('Valor Inválido!')
        break


def return_main():
    opcao_inv = input('(1) Retornar / (2) Inventário: ').strip()
    if opcao_inv == '1':
        game.norte_casa_1()
    elif opcao_inv == '2':
        inventory_main()
    else:
        print('Digite um valor válido!!')
        return_main()



if __name__ == "__main__":
    inventory_main()
