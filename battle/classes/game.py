import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS: " + bcolors.ENDC)
        i = 1
        for item in self.actions:
            print("\t" + str(i) + ": " + item)
            i += 1

    def choose_magic(self):
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC: " + bcolors.ENDC)
        i = 1
        for spell in self.magic:
            print("\t" + str(i) + ": " + spell.name + "(cost: " + str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ITEM: " + bcolors.ENDC)
        i = 1
        for item in self.items:
            print("\t" + str(i) + ". " + item["item"].name + ": " + item["item"].description + " (" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        for enemy in enemies:
            print("\t" + str(i) + ". " + enemy.name)
            i += 1
        choice = int(input("Choose tarrget: ") - 1)
        return choice

    def get_enemy_stats(self):
        hpbar = float(self.hp) / self.maxhp * 44

        hp = ""
        for i in range(0, 44):
            if i < hpbar:
                hp += u'\u2588'
            else:
                hp += " "

        hp_str = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_str) < 9:
            hp_str = " " + hp_str

        print("                      ____________________________________________")
        print(bcolors.BOLD + self.name + "      " + hp_str + " |" +
              bcolors.FAIL + hp + bcolors.ENDC +
              "|")

    def get_stats(self):
        hpbar = float(self.hp) / self.maxhp * 25
        mpbar = float(self.mp) / self.maxmp * 10

        hp = ""
        for i in range(0, 25):
            if i < hpbar:
                hp += u'\u2588'
            else:
                hp += " "

        mp = ""
        for i in range(0, 10):
            if i < mpbar:
                mp += u'\u2588'
            else:
                mp += " "

        hp_str = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_str) < 7:
            hp_str = " " + hp_str

        mp_str = str(self.mp) + "/" + str(self.maxmp)
        while len(mp_str) < 5:
            mp_str = " " + mp_str

        print("                      _________________________         __________")
        print(bcolors.BOLD + self.name + "      " + hp_str + " |" +
              bcolors.OKGREEN + hp + bcolors.ENDC +
              "| " + mp_str + " |" +
              bcolors.OKBLUE + mp + bcolors.ENDC + "|")