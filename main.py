import random

set_of_numbers_playerX = set()
set_of_numbers_playerO = set()
set_of_all_used_places = {1, 2, 3, 4, 5, 6, 7, 8, 9}
list_to_random = []
game = True
place = 0
place_in_playground = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

place1 = ""
place2 = ""
place3 = ""
place4 = ""
place5 = ""
place6 = ""
place7 = ""
place8 = ""
place9 = ""

win_combination = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]


# save position of sign for player

def player_choice(player, place_f):
    print(f'Select where you want to put {player}')
    place_f = int(input())
    while place_f not in (range(1, 10)):
        print('You must choose number in range 1-9!')
        print(f'Select where you want to put {player}')
        place_f = int(input())
    return place_f


# save position in list

def add_place_to_player(player, player_place, list_of_players_numbers, all_number_list):
    place_in_function = player_choice(player, player_place)
    list_of_players_numbers.add(place_in_function)
    all_number_list = all_number_list.discard(place_in_function)
    place_in_playground[place_in_function] = player


# save random position in list

def add_place_randomly(player, player_place, list_of_players_numbers, all_number_list):
    place_in_function = player_place
    list_of_players_numbers.add(place_in_function)
    all_number_list = all_number_list.discard(place_in_function)
    place_in_playground[place_in_function] = player


# print symbol on proper place

def print_table():
    print \
        (f'  {place_in_playground[1]}  |   {place_in_playground[2]}   |  {place_in_playground[3]}'
         f'                1 | 2 | 3')
    print('---------------------            ---------')
    print \
        (f'  {place_in_playground[4]}  |   {place_in_playground[5]}   |  {place_in_playground[6]}'
         f'                4 | 5 | 6')
    print('---------------------            ---------')
    print \
        (f'  {place_in_playground[7]}  |   {place_in_playground[8]}   |  {place_in_playground[9]}'
         f'                7 | 8 | 9')


# check that the game is finish

def check_who_win(list_of_player_numbers, player):
    global game
    if set_of_all_used_places == set():
        print('You used all places!!')
        game = False

    for subset in win_combination:
        if subset.issubset(list_of_player_numbers):
            print(f'Player {player} WIN !!!')
            game = False


print('Welcome to Tic Tac Toe Game!\n')
print(f'  {place1}   |   {place2}   |  {place3}                1 | 2 | 3')
print('---------------------          ---------')
print(f'  {place4}   |  {place5}    |  {place6}                4 | 5 | 6')
print('---------------------          ---------')
print(f'  {place7}   |  {place8}    |  {place9}                7 | 8 | 9')

# choose you want to play alone or with someone

print('Choose you want to play alone or with someone (1 or 2): ')
choose_player = int(input())
while choose_player < 1 or choose_player > 2:
    print('You need to choose between 1 or 2 players!')
    print('Choose you want to play alone or with someone (1 or 2): ')
    choose_player = int(input())

if choose_player == 1:
    while game:
        add_place_to_player(player='X', player_place=place, list_of_players_numbers=set_of_numbers_playerX,
                            all_number_list=set_of_all_used_places)
        print_table()
        check_who_win(list_of_player_numbers=set_of_numbers_playerX, player='X')

        if not game:
            break

        list_to_random = []

        for i in set_of_all_used_places:
            list_to_random.append(i)

        place = random.choice(list_to_random)

        add_place_randomly(player='O', player_place=place, list_of_players_numbers=set_of_numbers_playerO,
                           all_number_list=set_of_all_used_places)

        print_table()

        check_who_win(list_of_player_numbers=set_of_numbers_playerO, player='O')

        if not game:
            break


else:
    while game:
        add_place_to_player(player='X', player_place=place, list_of_players_numbers=set_of_numbers_playerX,
                            all_number_list=set_of_all_used_places)

        print_table()

        check_who_win(list_of_player_numbers=set_of_numbers_playerX, player='X')

        if not game:
            break

        add_place_to_player(player='O', player_place=place, list_of_players_numbers=set_of_numbers_playerO,
                            all_number_list=set_of_all_used_places)

        print_table()

        check_who_win(list_of_player_numbers=set_of_numbers_playerO, player='O')

        if not game:
            break
