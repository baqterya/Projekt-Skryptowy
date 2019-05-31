init python:
    class Player:
        def __init__(self, cha = 5, str = 5, wis = 5, infamy = 0, cash = 0, attack = 0,
            job = "", backg = "", cause = ""):
            self.cha = cha
            self.str = str
            self.wis = wis
            self.infamy = infamy
            self.attack = attack
            self.backg = backg
            self.cause = cause
            self.weapon = None
            self.clothing = None
            self.cash = cash

        def equip_weapon(self, weapon):
            if self.weapon != None:
                self.unequip_weapon()

            self.weapon = weapon
            self.attack = weapon.attack

        def unequip_weapon(self):
            if self.weapon != None:
                self.atk = 0
                self.weapon = None

        def equip_clothing(self, clothing):
            if self.clothing != None:
                self.unequip_clothing()

            self.clothing = clothing
            self.cha += clothing.cha_mod

        def unequip_clothing(self):
            if self.clothing != None:
                self.cha -= self.clothing.cha_mod
                self.clothing = None
