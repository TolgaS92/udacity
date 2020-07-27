import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("sorry, I don't understand."
                        "Please insert the right answer!")
    return response


def intro(enemie):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemie} is somewhere around here, "
                "and has been terrifying the nearby village...")
    print_pause("In front of you a house."
                "To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def cave(enemie, items):
    print_pause("You peer cautiously into the cave. "
                "It turns out to be only a very small cave. "
                "Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the sword of shadow hunter! ")
    print_pause("You discard your silly old dagger, "
                "and take the sword with you. "
                "You walk back out to the field.")
    if "sword" in items:
        print_pause("Already, You've got the sword, "
                    "there is nothing to do here!")
    else:
        print_pause("You have found the sword of shadow hunter!"
                    "You discard your silly old dagger, "
                    "and take the sword with you. "
                    "You walk back out to the field.")
        items.append("sword")
    field(enemie, items)


def house(enemie, items):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a {enemie}. "
                f"Oops! This is the {enemie} house! The {enemie} attacks you!")

    fight(enemie, items)


def fight(enemie, items):
    print_pause("Would you like to (1) fight or (2) run away?")
    response = valid_input(
        "(Please enter '1' or '2').\n",
        "1", "2")
    if response == '1':
        if "tunnel" in items:
            print_pause("You feel a bit under-prepared for this, "
                        "what with only having a tiny dagger.")
            print_pause("You do your best...")
            print_pause(f"But your dagger is no match for the {enemie}.\n"
                        "You have been DEFEATED!\n")
        else:
            if "sword" in items:
                print_pause(
                    f"As the {enemie} moves to attack, "
                    "you unsheath your new sword.\n"
                    "The sword of Ogoroth shines "
                    "brigthly in your hand \n"
                    "as you brace yourself for the attack.\n"
                    f"But the {enemie} takes one look at your "
                    "shiny new toy and runs away!\n"
                    f"You have rid the town of {enemie}.\n")
                print_pause("You're VICTORIOUS!\n")
                items.append("tunnel")
            else:
                print_pause("You feel a bit under-prepared for this, "
                            "what with only having a tiny dagger.")
                print_pause("You do your best...")
                print_pause(f"But your dagger is no match for the {enemie}.\n"
                            "You have been DEFEATED!\n")
                play_again()

    if response == '2':
        print_pause("You run back into the field. Luckily, you don't seem"
                    "to have been followed.")
        field(enemie, items)


def field(enemie, items):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?\n")
    response = valid_input(
        "(Please enter '1' or '2').\n",
        "1", "2")
    if response == '1':
        house(enemie, items)
    elif response == '2':
        cave(enemie, items)
    else:
        play_again()


def play_game():
    list_of_enemies = ['ogre', 'pirate', 'wicked farie', 'gorgon']
    enemie = random.choice(list_of_enemies)
    items = []
    intro(enemie)
    field(enemie, items)


def play_again():
    response = valid_input(
        "Would you like to play again?\n"
        "Please Enter 'yes' or 'no'.\n",
        "yes", "no")
    if response == "yes":
        play_game()
    if response == "no":
        exit()


play_game()


play_again()
