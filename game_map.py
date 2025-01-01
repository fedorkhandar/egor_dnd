"""
a map could have several layers:
1. tile type
2. items
3. creatures
4. fog of war
5. traps
6. doors
7. stairs
8. walls
9. decorations
10. light sources
11. sounds
12. weather

"""
# map

class TileType:
    title: str

class Tile:
    tile_type: TileType

    def __init__(self):
        self.tile_type = TileType()

class GameMap:
    tiles: list[list[Tile]]

    def __init__(self, width: int, height: int):
        self.tiles = [[Tile() for _ in range(width)] for _ in range(height)]

