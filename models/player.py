from dungeon_and_dragons.models.entity import Entity
from dungeon_and_dragons.systems.item_generator import generate_random_item, generate_item_by_rarity




class Player(Entity):
    def __init__(self, name, x, y, hp, max_hp,
                 attack_power, defense, level=1, exp=5, equipment_slots=[0, 0, 0, 0, 0, 0], inventory=[]): #slots - Это список являющийся инвентарём, и каждый отдельный индекс - определённая ячейка инвенторая (основная рука, голова, тело, ноги, вторая рука, амулет)
        super().__init__(name, x, y, hp, max_hp, attack_power, defense)
        self.level = level
        self.exp = exp
        self.next_level_exp = 20
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
                    player.inventory.append(item)



    def remove_item(self, slot):
        item = player.equipment_slots[slot]
        item.deactivate
        player.slots[slot] = 0



    def update_inventory(self):
        for item in self.equipment_slots:
            if item == 0:
                continue
            item.deactivate(self)
            item.activate(self)



player = Player(
            name="Hero",
            x=0, y=0,
            hp=30, max_hp=30,
            attack_power=5,
            defense=2
        )



