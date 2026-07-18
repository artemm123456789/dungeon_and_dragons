from dungeon_and_dragons.models.entity import Entity
from dungeon_and_dragons.systems.item_generator import generate_random_item, generate_item_by_rarity
import json



class Player(Entity):
    def __init__(self, name, x, y, hp, max_hp,
                 attack_power, defense, level=1, exp=5, next_level_exp=20, equipment_slots=[0, 0, 0, 0, 0, 0], inventory=[]): #slots - Это список являющийся инвентарём, и каждый отдельный индекс - определённая ячейка инвенторая (основная рука, голова, тело, ноги, вторая рука, амулет)
        super().__init__(name, x, y, hp, max_hp, attack_power, defense)
        self.level = level
        self.exp = exp
        self.next_level_exp = next_level_exp
        self.equipment_slots = equipment_slots
        self.inventory = inventory


    def get_item(self, item):
        if item.slot == None:
            self.inventory.append(item)
        else:
            if player.equipment_slots[item.slot] == 0:
                print(f"Получено: {item.name}")
                player.equipment_slots[item.slot] = item
                item.activate(self)
            else:
                if player.equipment_slots[item.slot].rarity > item.rarity:
                    print(f"Заменено: {player.equipment_slots[item.slot].name} на {item.name}")
                    player.equipment_slots[item.slot] = item
                    item.activate(self)
                else:
                    print(f"Вам выпал {item.name}, но слот занят {player.equipment_slots[item.slot].name}")



    def remove_item(self, slot):
        item = player.equipment_slots[slot]
        item.deactivate(self)
        player.slots[slot] = 0



    def update_inventory(self):
        for item in self.equipment_slots:
            if item == 0:
                continue
            item.deactivate(self)
            item.activate(self)

    def add_exp(self):
        self.max_hp += (self.max_hp // 10)
        self.attack_power += (self.attack_power // 4)
        self.defense += (self.defense // 4) #обнаружена проблема с defense, нацело не делится

    def save(self):
        with open('data/characteristics.json', 'w', encoding='utf-8') as f:
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
            self.next_level_exp = self.next_level_exp * 1.5
            self.save()




player = Player(
            name="Hero",
            x=0, y=0,
            hp=30, max_hp=30,
            attack_power=5,
            defense=2
        )





