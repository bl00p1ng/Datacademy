import math


def cylinder_volume(h, r):
    return round(math.pi * h * r**2, 2)


def sphere_volume(r):
    return round((4/3) * math.pi * r**3, 2)


def cube_volume(a):
    return round(a**3)


def cone_volume(h, r):
    return round((1 / 3) * math.pi * r**2 * h, 2)


def show_menu():
    msg = """
    → Elige la figura a la que quieres calcular su volúmen:
        ⤷ 1 - Cilindro
        ⤷ 2 - Esfera
        ⤷ 3 - Cubo
        ⤷ 4 - Cono
    """

    option = int(input(f'{msg}→ '))

    # Evaluate user's choise
    if option == 1:
        h = float(input(':: Ingresa la altura del cilindro: '))
        r = float(input(':: Ingresa el radio del cilindro: '))
        volume = cylinder_volume(h, r)
        show_result(volume, figure='Cilindro')
    elif option == 2:
        r = float(input(':: Ingresa el radio de la espera: '))
        volume = sphere_volume(r)
        show_result(volume, figure='Esfera')
    elif option == 3:
        a = float(input(':: Ingresa la longitud de la cara del cubo: '))
        volume = cube_volume(a)
        show_result(volume, figure='Cubo')
    elif option == 4:
        r = float(input(':: Ingresa el radio del cono: '))
        h = float(input(':: Ingresa la altura del cono: '))
        volume = cone_volume(h, r)
        show_result(volume, figure='Cono')
    else:
        print('\n⚠ Ingresaste una opción incorrecta, vuelve a intentarlo\n')
        main()


def show_result(volume, figure):
    print(f'\n→ Figura: {figure}\n→ Volúmen: {volume}')


def main():
    print(' CALCULADORA DE VOLÚMENES '.center(86, '*'))

    # Show menu and get data from the user
    show_menu()


if __name__ == '__main__':
    main()
