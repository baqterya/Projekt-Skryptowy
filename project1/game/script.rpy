# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define n = Character(None)
define g = Character("Gnom")

define t = Character("Terik")
default t_cha = 5   # charyzma
default t_str = 5   # siła
default t_int = 5   # intelekt
default t_inf = 0   # infamia
default cash = 0    # pieniądze
default t_job = ""
default t_background = ""
default t_cause = ""


# The game starts here.

label start:

    jump intro

    jump tavern


    # here goes the tavern scene

    return
