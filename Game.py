<py-script>
from js import document

inventory = []

rooms = {
    "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
    "Kitchen": {"north": "Hall", "item": "monster"},
    "Dining Room": {"west": "Hall", "south": "Garden", "item": "potion"},
    "Garden": {"north": "Dining Room"}
}

currentRoom = "Hall"

def print_to_terminal(text):
    term = document.getElementById("terminal")
    term.innerHTML += text + "\n"
    term.scrollTop = term.scrollHeight

def showInstructions():
    print_to_terminal("RPG Game")
    print_to_terminal("========")
    print_to_terminal("Get to the Garden with a key and a potion")
    print_to_terminal("Avoid the monsters!")
    print_to_terminal("")
    print_to_terminal("Commands:")
    print_to_terminal("go [direction]")
    print_to_terminal("get [item]")
    print_to_terminal("")

def showStatus():
    print_to_terminal("---------------------------")
    print_to_terminal("You are in the " + currentRoom)
    print_to_terminal("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print_to_terminal("You see a " + rooms[currentRoom]["item"])
    print_to_terminal("---------------------------")

def process_command(cmd):
    global currentRoom
    parts = cmd.lower().split()
    if not parts:
        return

    if parts[0] == "go":
        if len(parts) < 2:
            print_to_terminal("Go where?")
            return
        direction = parts[1]
        if direction in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][direction]
            if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "monster":
                print_to_terminal("The monster got you... GAME OVER!")
                return
        else:
            print_to_terminal("You can't go that way!")

    elif parts[0] == "get":
        if len(parts) < 2:
            print_to_terminal("Get what?")
            return
        item = parts[1]
        if "item" in rooms[currentRoom] and item == rooms[currentRoom]["item"]:
            inventory.append(item)
            print_to_terminal("You picked up the " + item)
            del rooms[currentRoom]["item"]
        else:
            print_to_terminal("Can't get " + item + "!")

    if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
        print_to_terminal("You escaped the house... YOU WIN!")
        return

    showStatus()

showInstructions()
showStatus()

def on_enter(event):
    if event.key == "Enter":
        cmd = document.getElementById("inputBox").value
        document.getElementById("inputBox").value = ""
        print_to_terminal("> " + cmd)
        process_command(cmd)

document.getElementById("inputBox").addEventListener("keydown", on_enter)
</py-script>
