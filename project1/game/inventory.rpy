init python:

    class Inventory_item:
        def __init__(self, name, img, val):
            self.name = name
            self.img = img
            self.val = val

    class Equipable(Inventory_item):
        def __init__(self, name, img, val):
            Inventory_item.__init__(self, name, img, val)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equipped = False
            self.equipped_to = None

    class Weapon(Equipable):
        def __init__(self, name, img, val, attack):
            Equipable.__init__(self, name, img, val)
            self.attack = attack

        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_weapon(self)

        def unequip(self):
            self.equipped_to.unequip_weapon()
            Equipable.unequip(self)

    class Clothing(Equipable):
        def __init__(self, name, img, val, cha_mod):
            Equipable.__init__(self, name, img, val)
            self.cha_mod = cha_mod

        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_clothing(self)

        def unequip(self):
            self.equipped_to.unequip_clothing()
            Equipable.unequip(self)
