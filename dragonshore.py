import items
import npc
import random
import enemies
import cinematics


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass


# ======= Blank enemy tile for testing
class BlankEnemy(MapTile):
    def __init__(self, x, y):
        self.exp_claimed = False
        self.enemy = enemies.LargeRat()
        self.alive_text = """
        Alive
        """
        self.dead_text = """
        Dead
        """
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            roll = random.randint(1, 20) + self.enemy.ab + self.enemy.str
            damage_roll = random.randint(1, self.enemy.damage) + self.enemy.str
            if roll >= player.ac:
                player.hp -= damage_roll
                print("Enemy rolled {}! It hits!".format(roll))
                print("Enemy does {} damage. You have {} HP remaining.\n".format(damage_roll, player.hp))
            else:
                print("Enemy rolled {}! It misses!\n".format(roll))
        elif not self.exp_claimed:
            self.exp_claimed = True
            player.exp += self.enemy.exp
            print("You gained {} exp! You now have {} total exp.\n".format(self.enemy.exp, player.exp))
            player.check_level()


# ======= Victory Tile for debugging purposes.
class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """


# ======= Generic Trader Tile for testing
class GenericTraderTile(MapTile):
    def __init__(self, x, y):
        # This is the NPC that resides on the tile.
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        try:
            for i, item in enumerate(seller.inventory, 1):
                print("{}. {} - {} Gold".format(i, item.name, item.value))
        except AttributeError:
            print("Selling items is a work in progress... I am so sorry.")
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except IndexError:
                    print("Nothing left to sell")
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        try:
            seller.inventory.remove(item)
        except AttributeError:
            if isinstance(item, items.Armor):
                seller.armor_inventory.remove(item)
            if isinstance(item, items.Weapon):
                seller.arms_inventory.remove(item)
            if isinstance(item, items.Consumable):
                seller.item_inventory.remove(item)
        try:
            buyer.inventory.append(item)
        except AttributeError:
            if isinstance(item, items.Armor):
                buyer.armor_inventory.append(item)
            if isinstance(item, items.Weapon):
                buyer.arms_inventory.append(item)
            if isinstance(item, items.Consumable):
                buyer.item_inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
        A friendly looking dwarf greets you.
        'What can I get fer ya?' He asks.
        """

