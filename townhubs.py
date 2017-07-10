import map
import items
import npc
import random
import enemies


class MapTile:
    # May have to call the player class so we can change quest statuses.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy = []

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass

        
class PlayerStartZone(MapTile):  # Just east of South Bismuth Road.
    def __init__(self, x, y):
        super().__init__(x, y)
        self.round_count = 0
        self.is_dangerous = False
        
       
    def intro_text(self):
        return """\nYou wake up. Your camp is destroyed. Dried blood cakes your head.
The last thing you remember is accepting a contract to escort a noble.
You aren't sure what happened, your head is foggy."""
        
    def title_text(self):
        return """\nYou are off the main road. It lies to the West. A forest to the East."""
        
    def modify_player(self, player):
        self.round_count += 1
        if self.round_count == 2:
            print("What are you doing just standing around?")
        else:
            return
        
        
class BismuthHills(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dangerous = False
        
    def intro_text(self):
        return """\nThe small town of Bismuth Hills. Known 
for the beautiful geology in the surrounding hills."""
    
    def title_text(self):
        # Title text can totally be conditional.
        return """\nYou are in the town of Bismuth Hills."""
    
    def modify_player(self, player):
        if player is not self.in_town:
            print("Player is not in town!")
        if player is self.in_town:
            print("Player is in town!")