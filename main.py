import random
def get_choices():
    player_choice = input("Elije entre piedra, papel, tijeras: ")
    options = ["piedra", "papel", "tijeras"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_win(player, computer):
    print(f"\nElegiste {player} y la IA eligió {computer}\n")
    if player == computer:
        return "Empatados!"
    elif player == "piedra":
        if computer == "tijeras":
            return "La piedra aplasta a las tijeras! Ganaste"
        else:
            return "El papel cubre a la roca, dijo un sabio"
    elif player == "papel":
        if computer == "piedra": 
            return "El papel cubre a la tijera, ganaste"
        else:
            return "Las tijeras cortan al papel, perdiste :("
    elif player == "tijeras":
        if computer == "papel":
            return "Las tijeras cortan al papel, ganaste :D"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
