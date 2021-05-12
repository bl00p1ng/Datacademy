def calculate_area(b, h):
    return (b * h) / 2


def classify_triangle(side_a, side_b, side_c):
    triangle_type = ''

    if side_a == side_b and side_b == side_c:
        triangle_type = 'Equilátero'
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_type = 'Isósceles'
    else:
        triangle_type = 'Escaleno'
    
    return triangle_type


def show_sides(sides):
    sides_msg = f"""
    ⤷ Lado A: {sides[0]}
    ⤷ Lado B: {sides[1]}
    ⤷ Lado C: {sides[2]}
    """
    print(sides_msg)

def main():
    print(' CALCULA EL ÁREA DE UN TRIÁNGULO '.center(83, '*'))

    b = float(input(':: Ingresa la base del triángulo: '))
    h = float(input(':: Ingresa la altura del triángulo: '))

    # Message used when the user enters the triangle's sides
    msg = """
    :: Ingresa los lados del triángulo separados por comas y un espacio.
    Por ejemplo: 2.3, 4, 5.4
    """

    sides = list(map(float, input(f'{msg}→ ').split(', ') ))
    show_sides(sides)

    # Show triangle area
    print(f'\n→ El área del Triángulo es {calculate_area(b, h)}')

    # Show triangle type
    print(f'→ El triángulo es {classify_triangle(sides[0], sides[1], sides[2])}')


if __name__ == '__main__':
    main()
