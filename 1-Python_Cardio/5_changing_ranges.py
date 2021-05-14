def compare_number(lower, upper, c_number):
    if c_number > lower and c_number < upper:
        print(f'\n→ El número {c_number} esta dentro del rango {lower} - {upper}')
    elif lower > upper or upper < lower:
        err_msg = """
        ⚠ Cometiste un error al ingresar los límites!
        Recuerda que el límite inferior no puede ser mayor que el superior y viceversa.
        🔁 Por favor intentalo nuevamente.
        
        """
        print(err_msg)
        show_menu()
    else:
        print(f'\n→ El número {c_number} NO esta dentro del rango {lower} - {upper}')
        show_menu()


def show_menu():
    lower_limit = int(input('\n:: Ingresa el límite inferior: '))
    upper_limit = int(input(':: Ingresa el límite superior: '))
    comparison_number = int(input(':: Ingresa el número de comparación: '))

    # Evaluate the number
    compare_number(lower_limit, upper_limit, comparison_number)


def main():
    print(' RANGOS CAMBIANTES '.center(69, '*'))

    # Show menu and get data from the user
    show_menu()


if __name__ == '__main__':
    main()
