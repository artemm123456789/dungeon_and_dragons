import json
from dungeon_and_dragons.models.entity import Entity

class Player(Entity):
    def __init__(self, name, x, y, hp, max_hp,
                 attack_power, defense, level=1, exp=0, next_level_exp=20):
        super().__init__(name, x, y, hp, max_hp, attack_power, defense)
        self.level = level
        self.exp = exp
        self.next_level_exp = next_level_exp * 1.5

    def add_exp(self):
        self.max_hp += (self.max_hp // 10)
        self.attack_power += (self.attack_power // 4)
        self.defense += (self.defense // 4)

    def save(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({"hp": self.hp,
                       "max_hp": self.max_hp,
                       "attack_power": self.attack_power,
                       "defense": self.defense,
                       "level": self.level,
                       "exp": self.exp,
                       "next_level_exp": self.next_level_exp}, f, ensure_ascii=False, indent=4)

    def next_level(self):
        if self.exp >= self.next_level_exp:
            self.level += 1
            self.add_exp()
            self.save()

