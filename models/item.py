from dungeon_and_dragons.data import items_functions


class Item:
    def __init__(self, name, rarity, function, reverse_function, slot):
        self.name = name
        self.rarity = rarity
        self.function = function
        self.reverse_function = reverse_function
        if slot == "":
            self.slot = None
        else:
            self.slot = slot

    def activate(self, player):
        if self.function:
            func_name = self.function
            if hasattr(items_functions, func_name):
                func = getattr(items_functions, func_name)
                func(player)

    def deactivate(self, player):
        if self.reverse_function:
            rev_func_name = self.reverse_function
            if hasattr(items_functions, rev_func_name):
                rev_func = getattr(items_functions, rev_func_name)
                rev_func(player)
