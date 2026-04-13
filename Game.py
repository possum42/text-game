def showInstructions():
    #print a main menu and the commands
    print(
        """
            RPG Game
            ========
            
            Get to the Garden with a key and a potion
            Avoid the monsters!
            
            Cofmmands:
            go [direction]
            get [item]
            """
        )

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
    'Kitchen' : {
        'north' : 'Hall',
        'item' : 'monster'
    },
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden',
        'item' : 'potion'
        },
    'Garden' : {
        'north' : 'Dining Room'
        }
}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever

# loop forever
while True:

    showStatus()

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]

            # MONSTER CHECK
            if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "monster":
                print("The monster got you... GAME OVER!")
                break

        else:
            print("You can't go that way!")

    # if they type 'get' first
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(' You picked up the ' + move[1])
            del rooms[currentRoom]['item']
        else:
            print("Can't get " + move[1] + "!")

    # win condition
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
            
        # after moving into a new room
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "monster":
            print("The monster got you... GAME OVER!")
            


