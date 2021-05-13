def show_menu():
    msg = """
    :: Elige una opción
       ⤷ 1 - Convertir de Millas a Kilómetros
       ⤷ 2 - Convertir de Kilómetros a Millas
    """

    option = int(input(f'{msg}→ '))
    amount_to_convert = 0.0

    if option == 1:
        amount_to_convert = float(input(':: Ingresa la cantidad de Millas que quieres convertir: '))
    elif option == 2:
        amount_to_convert = float(input(':: Ingresa la cantidad de kilómetros que quieres convertir: '))

    else:
        print('⚠ Ingresaste una opción incorrecta\n')
        main()

    return amount_to_convert, option


def show_results(amount, total, unit_original, unit_coversion):
    print(f'{amount}{unit_original} es igual a {total}{unit_coversion}')


def miles_to_km(mi):
    mile_in_km = 1.609344
    conversion = mi * mile_in_km

    return round(conversion, 2)

def km_to_miles(km):
    km_in_miles = 0.621371192237334
    conversion = km * km_in_miles

    return round(conversion, 2)



def main():
    print(' CONVERSOR DE DISTANCIAS '.center(75, '*'))

    # Show menu and get the conversion type (c_type)
    amount_to_convert, c_type = show_menu()

    if c_type == 1:
        total = miles_to_km(amount_to_convert)
        show_results(amount_to_convert, total, unit_original='mi', unit_coversion='km')

    elif c_type == 2:
        total = km_to_miles(amount_to_convert)
        show_results(amount_to_convert, total, unit_original='km', unit_coversion='mi')


if __name__ == '__main__':
    main()
