import random
from dungeon_and_dragons.models.entity import Entity
from dungeon_and_dragons.models.player import Player
from dungeon_and_dragons.models.monster import Monster



def melee_attack(attacker, defender):
    # attacker - это наш игрок. Его характеристики (урон, хп и так далее бери в player.py)
    # defender - это враг, его характеристики из monster.py
    """Эта функция должна возвращать итог удара
        f"⚔️ {attacker.name} бьет {defender.name} на {actual_damage} урона{crit_text} (Осталось HP: {defender.hp})"
        или
        f"💀 {attacker.name} уничтожает {defender.name} на {actual_damage} урона{crit_text}!"


        Урон должен считаться от атаки персонажа, плюс некоторая случайная вариативность (например, атака персонажа 5, но он может ударить на 6 или 7)
        При этом должна учитываться защита defender`a
        С некоторым шансом можно сделать критический удар
    """
    dmg = attacker.attack_power
    crit_multiplier = 1.5
    crit_chance = 20
    actual_damage = dmg

    ### ПОПРАВИТЬ (сделанно)

    defender_resist = 0
    armor_resistance_multiplier = 0.15 #изначальный множитель сопротивления за единицу брони
    for i in range(defender.defense):
        missing_absolute_resistance = 1 - defender_resist
        defender_resist += armor_resistance_multiplier * missing_absolute_resistance


    if random.randint(1, 10) <= 6:   #отклонение урона с шансом 60%, урон может варьироваться от 80% attack_power до 120% attack_power
        deviation_dmg = random.randint(-20, 20)/100
        actual_damage = round(dmg * (1 + deviation_dmg))

    if random.randint(1, 100) <= crit_chance:   #критические удары с шансом crit_chance
        actual_damage *= crit_multiplier
        actual_damage *= (1 - defender_resist)
        actual_damage = round(actual_damage)
        defender.take_damage(actual_damage)
        return f"⚔️ {attacker.name} бьет {defender.name} и наносит критические {actual_damage} урона! (Осталось HP: {defender.hp})"

    actual_damage *= (1 - defender_resist)
    actual_damage = round(actual_damage)
    defender.take_damage(actual_damage)
    return f"⚔️ {attacker.name} бьет {defender.name} на {actual_damage} урона (Осталось HP: {defender.hp})"


#hero = Player(name="Hero_test", x=1, y=1, max_hp=10, hp=10, attack_power=5, defense=5, level=1, exp=0)
#monster = Monster(name="Monster_test", x=1, y=1, hp=1000, attack_power=5, defense=1, exp=0)

#print(melee_attack(hero, monster))
