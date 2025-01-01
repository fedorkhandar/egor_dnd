"""
Simple DND

1. Path generation
2. NPC generation
3. Combat

"""

class Game:
    pass


# items

class Item:
    width: int
    height: int

class Weapon(Item):
    title: str
    damage: int

class Armor(Item):
    title: str
    defense: int

class Artifact(Item):
    title: str

class placedItem:
    x_left: int
    y_top: int
    item: Item

# inventory

class Inventory:
    width: int
    height: int
    items: list[placedItem]

# creatures

class Creature:
    title: str
    health: int = 100
    action_points: int = 3
    inventory: Inventory

class NPC(Creature):
    pass

class Player(Creature):
    pass    


