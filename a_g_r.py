import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def field_intro(creature):
    print_pause("You find yourself standing in an open field, "
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    print_pause("")


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def choice_house(items, creature):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a {creature} .")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")
    if "Sword" in items:
        print_pause("")
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    fight_run = valid_input("Would you like to (1) fight or (2) run away?",
                            ['1', '2'])
    if fight_run == '1':
        if "Sword" in items:
            print_pause(f"As the {creature} moves to attack,"
                        " you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly "
                        "in your hand as you brace yourself for the attack.")
            print_pause(f"But the {creature} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {creature}. "
                        "You are victorious!")
            game_replay(items, creature)
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {creature}.")
            print_pause("You have been defeated!")
            game_replay(items, creature)
    if fight_run == '2':
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        game_proper(items, creature)


def choice_cave(items, creature):
    print_pause("You peer cautiously into the cave.")
    if "Sword" in items:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        game_proper(items, creature)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("Sword")
        game_proper(items, creature)


def game_proper(items, creature):
        print_pause("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.\n"
                    "What would you do?\n")
        choice = valid_input("(Please enter 1 or 2.)", ['1', '2'])
        if choice == '1':
            choice_house(items, creature)
        if choice == '2':
            choice_cave(items, creature)


def game_replay(items, creature):
        print_pause("GAME OVER")
        replay = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
        if replay == 'y':
            items = ['']
            creature = random.choice(["troll", "dragon", "gogarith"])
            field_intro(creature)
            game_proper(items, creature)
        if replay == 'n':
            exit()


def play_game():
    creature = random.choice(["giant-elf", "monster", "dracula"])
    items = []
    field_intro(creature)
    game_proper(items, creature)
    game_replay(items)


play_game()
