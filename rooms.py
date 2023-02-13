# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# game controls
controls = ['North', 'South', 'East', 'West']

# Room player starts in
current_room = 'Great Hall'
print('You are in the {}.'.format(current_room))

# game instructions
game_instructions = 'To play this game you simple have to make your way from through the rooms. The commands you may ' \
                    'use to navigate through the rooms are North, South, East, and West. Be careful not to make a ' \
                    'wrong turn. To leave the game just head to the exit by inputting Exit Game. Have fun!'
print(game_instructions)

# loop for game
while True:
    user_input = input('Which direction next? ')
    direction = user_input

    # To exit game
    if user_input == 'Exit Game':
        print('\nGame Over. Come back and play again anytime.\n')
        break
    if direction in controls:
        if direction in rooms[current_room]:
            if current_room == 'Great Hall':
                current_room = rooms[current_room][direction]
            elif current_room == 'Bedroom':
                current_room = rooms[current_room][direction]
            elif current_room == 'Cellar':
                current_room = rooms[current_room][direction]
        else:
            # Invalid command
            print('\nWrong way. Try a different move.')
    else:
        # Invalid command
        print('\nInvalid command. Try again.')

    # print current room
    print('\nYou are in the {}.'.format(current_room))