from dungeon_and_dragons.models.entity import Entity

class Player(Entity):
    def __init__(self, name, x, y, hp, max_hp,
                 attack_power, defense, level=1, exp=0):
        super().__init__(name, x, y, hp, max_hp, attack_power, defense)
        self.level = level
        self.exp = exp
        self.next_level_exp = 10

    def add_exp(self):
        (self.max_hp // 10) + self.max_hp
        (self.attack_power // 4) + self.attack_power
        (self.defense // 4) + self.defense

    def next_level(self):
        if self.exp >= self.next_level_exp:
            self.level += 1
            (self.next_level_exp // 2) + self.next_level_exp
            self.add_exp()