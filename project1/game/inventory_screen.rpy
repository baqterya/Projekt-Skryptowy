style inventory_style:

    xalign 0.5

style slot:
    background Frame("square", 0, 0)
    minimum(80, 80)
    maximum(80, 80)
    xalign 0.1

screen inventory_button:
        textbutton "Ekwipunek" action Show("inventory_screen")  text_size 18

screen inventory_screen:
    style_prefix "inventory"

    add "white"
    #hbox:
    #cash
    vbox:
        xalign 0.05
        xmaximum 400
        spacing 10
        label "{color=#000}Posiadane pieniądze:" xalign 0.5 text_size 16
        label "{color=#000}[pc.cash] dukatów" text_size 16

        # equipped weapon
        label "{color=#000}\n\nUbrane przedmioty:" text_size 16
        frame:
            style "slot"
            if pc.weapon != None:
                add pc.weapon.img
            else:
                label "{color=#000}broń" xalign 0.5 yalign 0.5 text_size 12
        # equipped clothing
        frame:
            style "slot"
            if pc.clothing !=None:
                add pc.clothing.img
            else:
                label "{color=#000}strój" xalign 0.5 yalign 0.5 text_size 12

    # inventory grid
    grid 5 5:
        xalign 0.3
        yalign 0.2
        spacing 5
        for item in inventory:
            frame:
                style "slot"
                imagebutton idle item.img action SetVariable("selected_item", item)
        for i in range(len(inventory), 25):
            frame:
                style "slot"

    # item details
    vbox:
        xalign 0.69
        spacing 15
        if selected_item != None:
            label "{color=#000}[selected_item.name]" xalign 0.5 text_size 16
            frame:
                style "slot"
                add selected_item.img

            label "{color=#000}Wartość przedmiotu: [selected_item.val]" text_size 16

            if isinstance(selected_item, Equipable):
                if selected_item.is_equipped:
                    textbutton "{color=#000}Zdejmij":
                        action Function(selected_item.unequip)
                    textbutton "{color=#000}Wyrzuć":
                        xalign 10
                        yalign 0.9
                        action Function(selected_item.unequip), RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)
                        text_size 16
                else:
                    textbutton "{color=#000}Wyposaż":
                        action Function(selected_item.equip, pc)
                    textbutton "{color=#000}Wyrzuć":
                        action RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)
                        text_size 16
            else:
                textbutton "{color=#000}Wyrzuć":
                    action RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)
                    text_size 16

        else:
            label "{color=#000}Brak wybranego przedmiotu" xalign 0.5 text_size 16

    textbutton "{color=#000}Zamknij":
        action Hide("inventory_screen")
        xalign 0.5
        yalign 0.78
