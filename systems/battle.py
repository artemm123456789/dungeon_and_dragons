import random
from models.entity import Entity


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

