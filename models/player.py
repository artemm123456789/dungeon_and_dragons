from dungeon_and_dragons.models.entity import Entity

class Player(Entity):
    def __init__(self, name, x, y, hp, max_hp,
                 attack_power, defense, level=1, exp=5):
        super().__init__(name, x, y, hp, max_hp, attack_power, defense)
        self.level = level
        self.exp = exp
        self.next_level_exp = 20