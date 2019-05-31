define narrator = nvl_narrator
define n = Character(None)
define g = Character("Gnom")

default inventory = []
default selected_item = None
default pc = Player()


# The game starts here.

label start:

    show screen inventory_button    # przycisk otwierający Ekwipunek

    jump intro

    jump tavern


    # here goes the tavern scene

    return
