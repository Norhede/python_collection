import random


class Color:
    end = '\x1b[0m'
    # bold = '\x1b[1m'
    underline = '\x1b[4m'
    red = '\033[1;31m'
    green = '\033[1;32m'
    orange = '\033[1;33m'
    blue = '\033[1;34m'
    purple = '\033[1;35m'
    darkcyan = '\x1b[1;36m'
    yellow = '\x1b[1;93m'
    cyan = '\x1b[1;96m'


class Player:
    attack = 1
    defence = 1
    health = 5
    gold = 0
    weapon = dict()
    armor = dict()


class Monster:
    name: ''
    attack: 0
    defence: 0
    health: 0
    gold: 0
    monster_list = []
    # Monsters are added in by a list : ['name', attack, defence, health, gold drop]
    monster_list.append(['Monster 1', 0, 0, 5, 1])
    monster_list.append(['Monster 2', 1, 1, 5, 2])
    monster_list.append(['Monster 3', 2, 2, 10, 3])
    monster_list.append(['Monster 4', 4, 4, 25, 4])
    monster_list.append(['Monster 5', 10, 10, 100, 5])


class Item:
    # Items are added in by a list : [id, 'name', stat_value]
    weapon_list = []
    weapon_list.append([1, 'Beginner\'s sword', 1])
    weapon_list.append([2, 'Longsword', 2])
    weapon_list.append([3, 'Greatsword', 3])

    armor_list = []
    armor_list.append([1, 'Beginner\'s armor', 1])
    armor_list.append([2, 'Leather armor', 2])
    armor_list.append([3, 'Plated armor', 3])


def roll_random(min_value, max_value):
    random_number = int(random.randint(min_value, max_value))
    print(random_number)
    for i in range(len(Item.weapon_list)):
        if random_number == Item.weapon_list[i][0]:
            print(Item.weapon_list[i][1])
        else:
            print("No")


def welcome_text():
    print('\n-----')
    print('Hello, and welcome to a short demonstration of basic Python rpg')
    print("In this demonstration, the user (that's you!) chooses what happens depending on the the input given.")
    print('Feel free to mess around - if you accidentally quit the program, you can run it again using Shift+F10')
    print('-----\n')


def color_test():
    print(Color.red + "1234567890")
    print(Color.green + "1234567890")
    print(Color.orange + "1234567890")
    print(Color.blue + "1234567890")
    print(Color.purple + "1234567890")
    print(Color.darkcyan + "1234567890")
    print(Color.yellow + "1234567890")
    print(Color.cyan + "1234567890" + Color.end)


def start_program():
    while True:
        command = input('Type in your input. (' + Color.cyan + 'help' + Color.end + ' for a list of commands)\n') + ''
        command = command.lower()
        check_command(command)


def choose_help():
    print('The following inputs are valid commands:')
    print('|  ' + Color.red + 'stats' + Color.end + '  |  ' + Color.blue + 'fight' + Color.end + '  ', end='')
    print('|  ' + Color.purple + 'buy' + Color.end + '  |  ' + Color.cyan + 'quit' + Color.end + '  |' + Color.end)
    start_program()


def back_quit():
    print('Type ' + Color.cyan + 'back' + Color.end + ' to go back or ' + Color.cyan + 'quit' + Color.end + ' to quit.')


def choose_stats():
    print('|  ' + Color.red + "Attack: " + str(Player.attack) + Color.end + '  ', end='')
    print('|  ' + Color.blue + "Defence: " + str(Player.defence) + Color.end + '  ', end='')
    print('|  ' + Color.purple + "Health: " + str(Player.health) + Color.end + '  ', end='')
    print('|  ' + Color.yellow + "Gold: " + str(Player.gold) + Color.end + '  |')
    start_program()


def choose_fight():
    back_quit()
    print('To fight a monster, type which level you would like to face (', end='')
    monster_level = input(Color.cyan + '1-5' + Color.end + ')\n') + ''
    if monster_level == 'back':
        start_program()
    if monster_level == 'quit':
        choose_quit()
    try:
        int(monster_level)
    except ValueError:
        print(Color.red + "I'm sorry, I don't recognize that input - please try again!" + Color.end)
        choose_fight()
    if 0 < int(monster_level) < len(Monster.monster_list)+1:
        fight_monster(monster_level)
    elif int(monster_level) > len(Monster.monster_list) or int(monster_level) < 1:
        print(Color.red + "You typed a wrong value, try again" + Color.end)
        choose_fight()
    else:
        print(Color.red + "Don't know how you got here, taking you back to the main menu.." + Color.end)
        start_program()


def choose_buy():
    back_quit()
    print("You can buy stat upgrades here! Your buy options are: ")
    print('+1 ' + Color.red + 'attack' + Color.end + ' for 5 ' + Color.yellow + 'gold' + Color.end + '.')
    print('+1 ' + Color.blue + 'defence' + Color.end + ' for 5 ' + Color.yellow + 'gold' + Color.end + '.')
    print('+5 ' + Color.purple + 'health' + Color.end + ' for 10 ' + Color.yellow + 'gold' + Color.end + '.')
    buy_input = input("Type in what you would like to buy\n")
    check_buy(buy_input)


def check_buy(buy_option):
    if buy_option is None or len(buy_option) < 1:
        print(Color.red + "I'm sorry, I didn't recieve any input - please try again!\n" + Color.end)
    elif buy_option == 'back':
        start_program()
    elif buy_option == 'quit':
        choose_quit()
    elif buy_option == 'attack':
        buy_upgrade('attack')
    elif buy_option == 'defence':
        buy_upgrade('defence')
    elif buy_option == 'health':
        buy_upgrade('health')
    else:
        print("I'm sorry, I don't know that command - try again!")
        choose_buy()


def buy_upgrade(option):
    if option == 'attack' and Player.gold > 4:
        Player.gold -= 5
        Player.attack += 1
        print("You've bought an " + Color.red + "attack " + Color.end + "upgrade!")
        choose_buy()
    elif option == 'defence' and Player.gold > 4:
        Player.gold -= 5
        Player.defence += 1
        print("You've bought a " + Color.blue + "defence " + Color.end + "upgrade!")
        choose_buy()
    elif option == 'health' and Player.gold > 9:
        Player.gold -= 10
        Player.health += 5
        print("You've bought a " + Color.purple + "health " + Color.end + "upgrade!")
        choose_buy()
    else:
        print(Color.red + "You don't have enough gold for this upgrade!" + Color.end)
        choose_buy()


def choose_quit():
    print(Color.cyan + Color.underline + 'Thank you for taking your time to view this demonstration.' + Color.end)
    quit()


def wrong_command():
    print(Color.red + "I'm sorry, I don't recognize that command - please try again!" + Color.end)


def check_command(user_input):
    if user_input is None or len(user_input) < 1:
        print(Color.red + "I'm sorry, I didn't recieve any input - please try again!\n" + Color.end)
    elif user_input == 'help':
        choose_help()
    elif user_input == 'stats':
        choose_stats()
    elif user_input == 'fight':
        choose_fight()
    elif user_input == 'buy':
        choose_buy()
    elif user_input == 'quit':
        choose_quit()
    else:
        wrong_command()
        start_program()


def fight_monster(level):
    choice = int(level)
    Monster.name = Monster.monster_list[choice-1][0]
    Monster.attack = Monster.monster_list[choice-1][1]
    Monster.defence = Monster.monster_list[choice-1][2]
    Monster.health = Monster.monster_list[choice-1][3]
    Monster.gold = Monster.monster_list[choice-1][4]
    if Player.attack - Monster.defence <= 0:
        print("You lose to " + Color.red + Monster.name + Color.end + ", try an easier monster!")
        choose_fight()
    elif Monster.attack - Player.defence <= 0:
        print("You win over " + Color.red + Monster.name + Color.end + "! ", end='')
        print("Here, have " + Color.yellow + str(Monster.gold) + " gold" + Color.end + "!")
        Player.gold += Monster.gold
        choose_fight()
    elif (Monster.health / (Player.attack - Monster.defence)) < (Player.health / (Monster.attack - Player.defence)):
        print("You win over " + Color.red + Monster.name + Color.end + " ! ", end='')
        print("Here, have " + Color.yellow + str(Monster.gold) + " gold" + Color.end + "!")
        Player.gold += Monster.gold
        choose_fight()
    elif (Player.health / (Monster.attack - Player.defence)) < (Monster.health / (Player.attack - Monster.defence)):
        print("You lose to " + Monster.name + ", try an easier monster!")
        choose_fight()


def main():
    start_program()


welcome_text()
main()


# create variables for attack, defence, health, gold - DONE
# create fight option - DONE
# create error handling for string conversion to int - DONE
# create buy option - DONE
# expand fight option to multiple monsters - DONE
# expand fight option to a list of monsters with static stats not based on multiplication - DONE
# Work with the RNG, make it reusable for multiple purposes
# create drop table for monster
# create inventory variable (list)
# expand drop table for monster to include weapon and armor (static gear)
# expand drop table to randomize values on gear (dynamic gear)
