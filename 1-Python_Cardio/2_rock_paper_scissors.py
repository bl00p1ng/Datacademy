def game(option_player_1, option_player_2, score_player_1, score_player_2):
    game_result = ''

    if option_player_1 == option_player_2:
        game_result = '⚠ Empate'
        score_player_1 += 1
        score_player_2 += 1

    elif option_player_1 == 'piedra':
        if option_player_2 == 'papel':
            game_result = '☑ El Jugador 2 GANA'
            score_player_2 += 1
        elif option_player_2 == 'tijera':
            game_result = '☑ El Jugador 1 GANA'
            score_player_1 += 1

    elif option_player_1 == 'papel':
        if option_player_2  == 'piedra':
            game_result = '☑ El Jugador 1 GANA'
            score_player_1 += 1
        elif option_player_2 == 'tijera':
            game_result = '☑ El Jugador 2 GANA'
            score_player_2 += 1

    elif option_player_1 == 'tijera':
        if option_player_2 == 'piedra':
            game_result = '☑ El Jugador 2 GANA'
            score_player_2 += 1
        elif option_player_2 == 'papel':
            game_result = '☑ El Jugador 1 GANA'
            score_player_1 += 1

    else:
        game_result = '⚠ Elegiste una opción incorrecta'

    return game_result, score_player_1, score_player_2


def main():
    print(' PIEDRA, PAPEL O TIJERA '.center(74, '*'))

    # Save the score of each player
    score_player_1 = 0
    score_player_2 = 0


    # Run game
    game_session = 0
    while game_session < 3:

        msg = """
        → Elige una opción:
        ⤷ Piedra
        ⤷ Papel
        ⤷ Tijera
        """
        option_player_1 = input(f':: JUGADOR 1 {msg}→ ').lower()
        option_player_2 = input(f'\n:: JUGADOR 2 {msg}→ ').lower()
        
        result, score_player_1, score_player_2 = game(
            option_player_1,
            option_player_2,
            score_player_1,
            score_player_2)

        # Show game results
        print(f'\n {result} esta ronda\n')

        game_session += 1

    # Show winner
    if score_player_1 > score_player_2:
        print('\n🏆 El Jugador 1 GANA la partida')
    elif score_player_1 == score_player_2:
        print('\n ⚠ Empate')
    else:
        print('\n🏆 El Jugador 2 GANA la partida')


if __name__ == '__main__':
    main()