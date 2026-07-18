from dataclasses import dataclass

@dataclass
class Entity:
    def __init__(self, name, x, y, hp, max_hp, attack_power=5, defense=1, is_alive=True):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.attack_power = attack_power
        self.defense = defense
        self.is_alive = is_alive

    def take_damage(self, damage):
        actual_damage = damage
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        return actual_damage
