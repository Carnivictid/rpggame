import map
import items
import npc
import random
import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy = []

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")
    
    def title_text(self):
        return """\nNo title text has been created."""

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dangerous = True
        self.enemy = [enemies.LargeRat(),
                      enemies.SmallGoblin()]

    def intro_text(self):
        return """\nThe stench of death and rot are all around you."""
    
    def title_text(self):
        return """This is the starting tile!"""

    def modify_player(self, player):
        attack_pool = []
        attack_pool.append(player)
        for member in player.party:
            attack_pool.append(member)
            
        if len(self.enemy) > 0:
            for number, monster in enumerate(self.enemy, 1):
                if monster.is_dead():
                    self.enemy.remove(monster)
                elif monster.is_alive():
                    chance = random.randint(1, len(attack_pool)) - 1
                    monster.attack_player(attack_pool[chance], number)
        if len(self.enemy) <= 0:
            self.is_dangerous = False
