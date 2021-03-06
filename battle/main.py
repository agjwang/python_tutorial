from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

import random

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 240, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 100)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 0)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 0)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos: ", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nicki: ", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot: ", 460, 65, 60, 34, player_spells, player_items)

# Instantiate Enemies
enemy1 = Person("Imp  ", 1200, 65, 45, 25, [], [])
enemy2 = Person("Magus", 1200, 65, 45, 25, [], [])
enemy3 = Person("Imp  ", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

running = True
while running:
    print("====================")

    print("\n")
    print("NAME:                 HP:                               MP:")
    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n")

    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == -1:
            continue
        elif index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked for " + str(dmg) + " points of damage")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            cost = spell.cost

            current_mp = player.get_mp()

            if cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(cost)
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_dmg) + " points of damage " + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg) + " points of damage " + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + bcolors.OKGREEN + item.name + " heals for " + str(item.prop) + " HP " + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "MegaElixir":
                    for p in players:
                        p.hp = p.maxhp
                        p.mp = p.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print("\n" + bcolors.OKGREEN + item.name + " fully restores HP/MP " + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print("\n" + bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage " + bcolors.ENDC)
        else:
            continue

    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)

    print("Enemy attacked for " + str(enemy_dmg) + " points of damage. Enemy HP: " + str(player1.get_hp()))

    if enemies[0].get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False
