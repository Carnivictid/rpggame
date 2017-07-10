import items


class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 350
        self.inventory = [items.LightHealingPotion(),
                          items.LightHealingPotion(),
                          items.PaddedArmor(),
                          items.LeatherArmor(),
                          items.StuddedLeather(),
                          items.ChainShirt(),
                          items.Dagger(),
                          items.ShortSword()]


class DragonShoreGuard(NonPlayableCharacter):
    def __init__(self):
        self.name = "Dragonshore Guard"
        self.gold = 1337