import random

from dungeon_and_dragons.models.item import Item
import json
import os


def load_items_templates():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'items.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_random_item():
    items_list = load_items_templates()
    item_data = random.choice(items_list)
    item = Item(
        name=item_data["name"],
        rarity=item_data["rarity"],
        function=item_data["function"],
        reverse_function=item_data["reverse_function"],
        slot=item_data["slot"]
    )
    return item


def generate_item_by_rarity(rarity):
    items_list = load_items_templates()
    for i in load_items_templates():
        if i["rarity"] != rarity:
            items_list.remove(i)
    item_data = random.choice(items_list)
    item = Item(
        name=item_data["name"],
        rarity=item_data["rarity"],
        function=item_data["function"],
        reverse_function=item_data["reverse_function"],
        slot=item_data["slot"]
    )
    return item


def generate_random_drop_from_monster(exp):
    base_weights = [50, 35, 10, 5]
    weights = base_weights
    for i in base_weights:
        bonus_weight = exp/10 * (base_weights.index(i) + 1)
        weights[base_weights.index(i)] = int((i + bonus_weight) * 10)

    rarity = int(random.choices(range(len(weights)), weights=weights, k=1)[0]) + 1

    return generate_item_by_rarity(rarity)




