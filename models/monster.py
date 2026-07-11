from dungeon_and_dragons.models.entity import Entity

class Monster(Entity):
    def __init__(self, name, x, y, hp, attack_power, defense, exp):
        super().__init__(name, x, y, hp, hp, attack_power, defense)
        self.exp = exp