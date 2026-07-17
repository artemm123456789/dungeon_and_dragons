
def test_equip1_func(player):
    player.attack_power += 2
    print("атака увеличенна на 2")

def test_equip1_rev_func(player):
    player.attack_power -= 2



def test_equip2_func(player):
    player.attack_power += 4
    print("атака увеличенна на 4")

def test_equip2_rev_func(player):
    player.attack_power -= 4



def test_equip3_func(player):
    player.defense += 2
    print("защита увеличенна на 2")

def test_equip3_rev_func(player):
    player.defense -= 2



def wooden_sword_func(player):
    player.attack_power += 1

def wooden_sword_rev_func(player):
    player.attack_power -= 1



def steel_sword_func(player):
    player.attack_power += 3

def steel_sword_rev_func(player):
    player.attack_power -= 3



def ancient_sword_func(player):
    player.attack_power += 5

def ancient_sword_rev_func(player):
    player.attack_power -= 5



def hero_sword_func(player):
    player.attack_power += 10

def hero_sword_rev_func(player):
    player.attack_power -= 10



def leather_helmet_func(player):
    player.defense += 1

def leather_helmet_rev_func(player):
    player.defense -= 1



def steel_helmet_func(player):
    player.defense += 2

def steel_helmet_rev_func(player):
    player.defense -= 2



def ancient_helmet_func(player):
    player.defense += 3

def ancient_helmet_rev_func(player):
    player.defense -= 3



def hero_helmet_func(player):
    player.defense += 5
    player.max_hp += 10

def hero_helmet_rev_func(player):
    player.defense -= 5
    player.max_hp -= 10



def leather_armor_func(player):
    player.defense += 2

def leather_armor_rev_func(player):
    player.defense -= 2



def steel_armor_func(player):
    player.defense += 4
    player.max_hp += 5

def steel_armor_rev_func(player):
    player.defense -= 4
    player.max_hp -= 5



def ancient_armor_func(player):
    player.defense += 6
    player.max_hp += 10

def ancient_armor_rev_func(player):
    player.defense -= 6
    player.max_hp -= 10



def hero_armor_func(player):
    player.defense += 10
    player.max_hp += 20

def hero_armor_rev_func(player):
    player.defense -= 10
    player.max_hp -= 20



def leather_boots_func(player):
    player.defense += 1

def leather_boots_rev_func(player):
    player.defense -= 1



def steel_boots_func(player):
    player.defense += 2

def steel_boots_rev_func(player):
    player.defense -= 2



def ancient_boots_func(player):
    player.defense += 3

def ancient_boots_rev_func(player):
    player.defense -= 3



def hero_boots_func(player):
    player.defense += 4
    player.max_hp += 5

def hero_boots_rev_func(player):
    player.defense -= 4
    player.max_hp -= 5



def wooden_shield_func(player):
    player.defense += 2

def wooden_shield_rev_func(player):
    player.defense -= 2



def steel_shield_func(player):
    player.defense += 3

def steel_shield_rev_func(player):
    player.defense -= 3



def ancient_shield_func(player):
    player.defense += 5

def ancient_shield_rev_func(player):
    player.defense -= 5



def hero_shield_func(player):
    player.defense += 7
    player.attack_power += 5

def hero_shield_rev_func(player):
    player.defense -= 7
    player.attack_power -= 5



def amulet_of_health_func(player):
    player.max_hp += 5

def amulet_of_health_rev_func(player):
    player.max_hp -= 5



def amulet_of_defense_func(player):
    player.defense += 3

def amulet_of_defense_rev_func(player):
    player.defense -= 3



def amulet_of_attack_func(player):
    player.attack_power += 5

def amulet_of_attack_rev_func(player):
    player.attack_power -= 5



def amulet_of_hero_func(player):
    player.attack_power += 5
    player.defense += 3
    player.max_hp += 10

def amulet_of_hero_rev_func(player):
    player.attack_power -= 5
    player.defense -= 3
    player.max_hp -= 10
