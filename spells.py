


class DamageSpell:
    def __init__(self):
        raise NotImplementedError("Do not create raw Spell objects")

    def __str__(self):
        return "L{}|{}: {}D{}".format(
                self.level, self.name, self.dice_amount, self.dice_number, self.level)


class BuffSpell:
    def __init__(self):
        raise NotImplementedError("Do not create raw Spell objects")

    def __str__(self):
        return "L{}|{}: {}".format(
                self.level, self.name, self.type)


# ======= 1 Level spells ======= #
class BurningHand(DamageSpell):
    def __init__(self):
        self.name = "Burning Hands"
        self.dice_amount = 1
        self.dice_number = 4
        self.level = "1"
        self.type = "damage"
        self.lasts_rounds = 1


class MageArmor(BuffSpell):
    def __init__(self):
        self.name = "Mage Armor"
        self.dice_amount = 1
        self.dice_number = 4
        self.level = "1"
        self.type = "buff"
        self.lasts_rounds = 15


class ShockingGrasp(DamageSpell):
    def __init__(self):
        self.name = "Shocking Grasp"
        self.dice_amount = 1
        self.dice_number = 6
        self.level = "1"
        self.type = "damage"
        self.lasts_rounds = 1


# ======= 0 Level Spells ======= #
class RayOfFrost(DamageSpell):
    def __init__(self):
        self.name = "Ray of Frost"
        self.dice_amount = 1
        self.dice_number = 3
        self.level = "0"
        self.type = "damage"
        self.lasts_rounds = 1
