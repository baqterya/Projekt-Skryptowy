label intro:
    "Rozpoczynasz swoją przygodę jako ludzki kupiec z leżącej na północy Federacji Lyvsik"

    $ inventory.append(water_bag)

    "Wychowałeś się w: "
    menu (nvl=True):
        "Mieszczańskiej rodzinie ze stolicy":
            python:
                pc.backg = "burgher"
                pc.cash = 50
                pc.wis += 1
                pc.cha += 1
                inventory.append(b_clothing)
            jump intro_1

        "Pomniejszym rodzie szlacheckim":
            python:
                pc.backg = "noble"
                pc.cash = 120
                pc.wis += 1
                pc.infamy -= 2
                inventory.append(n_clothing)
            jump intro_1

        "Ubogiej rodzinie z podgrodzia":
            python:
                pc.backg = "peasant"
                pc.cash = 18
                pc.wis += 2
                pc.cha -= 2
                inventory.append(p_clothing)
            jump intro_1


    label intro_1:
        nvl clear

        if pc.backg == "burgher":
            "Większość swojego życia spędziłeś w Lysvik - stolicy Federacji ludzi, krasnoludów i gnomów zamieszkujących północ Arrionu."
            "Tam właśnie wychowałeś się w rodzinie jednego z licznych Lysvickich kupców. Od kiedy pamiętasz podziwiałeś przedsiębiorczość"
            "ojca i szybko poszedłeś w jego ślady. Widząc w tobie potencjał, wysłał cię na nauki u swojego starego mistrza."
            nvl clear
            "W końcu po latach nauki zostałeś oficjalnym członkiem gildii handlowej. Teraz czeka cię twoje pierwsze poważne zadanie:"
            "Musisz udać się w długą podróż do Wolnego Miasta Urdinas."

        elif pc.backg == "noble":
            "Wychowałeś się w wysokich sferach Lysvik - stolicy Federacji ludzi, krasnoludów i gnomów zamieszkujących północ Arrionu."
            "Chociaż twój ród nie należy do najbardziej wpływowych politycznie to twój ojciec jest poważnym udziałowcem gildii handlowej."
            "Od kiedy pamiętasz zawsze zależało mu na budowie prestiżu rodu więc zapewnił ci, jako swojemu następcy, najlepszą możliwą edukację."
            "Zarówno on jak i gildia handlowa pokładają w tobie nadzieję, bo to od ciebie będzie zależeć wasza przyszła współpraca."
            nvl clear
            "Po ukończeniu szkolenia zostałeś wybrany do swojej pierwszej ważnej misji. "
            "Masz za zadanie jak najszybciej dotrzeć do Urdinas - Miasta Gildii aby
             spotkać się z przedstawicielami Jedwabnego Liścia - najbardziej wpływowej gildii handlowej na całym kontynencie."

        elif pc.backg == "peasant":
            "Pochodzisz z podgrodzi  Lysvik - stolicy Federacji ludzi, krasnoludów i gnomów zamieszkujących północ Arrionu."
            "Twoja rodzina, chociaż wciąż uboga, była jedną z bardziej liczących się w jednej z podlysvickich wsi."
            "Twój ojciec był szanowanym przez społeczność myśliwym a matka była znana ze swojej wiedzy na temat ziół"
            "Na dodatek bliskim przyjacielem twojego ojca był wiejski kowal."
            nvl clear
            "Zdeterminowany aby wyrwać się z rodzinnej mieściny od najmłodszych lat chłonąłeś wiedzę od każdego czeladnika w wiosce."
            "W końcu, kiedy dorosłeś postanowiłeś, że czas spróbować szczęścia w wielkim świecie i wyruszyć w podróż."
            "Załadowawszy wóz towarem i pożegnawszy rodzinę i przyjaciół wyruszasz na wschód do Urdinas - miasta nieskończonych możliwości."

        jump intro_2


    label intro_2:
        nvl clear

        "Wolne Miasto Udrinas, znane także jako Miasto Gildii to największa metropolia na całym kontynencie."
        "Podróżnicy mawiają, że rozpościera się ono na powierzchni niewielkiego kraju a przejście z jednego końca na drugi może trwać nawet trzy dni."
        "Leżące na wschodnim wybrzeżu Urdinas jest miejscem ściągającym rocznie niezliczone ilości przyjezdnych szukających szczęścia w metropolii."
        nvl clear
        "W Lysvik krążyły pogłoski o tym, że Urdinas daje szansę każdemu kto ma coś do pokazania a większość rządzących miastem Gildii
         nie przykłada nawet uwagi do rasy przybyszów."
        "Dlatego to właśnie tam ściągają udolnieni kupcy, wynalazcy ograniczani przez rodzinne kraje, najemnicy szukający lepszych zarobków czy
         kapłani poszukujący nowych wiernych."
        "Tu także wielu przyjezdnych próbuje na nowo rozpocząć swoje życie."
        nvl clear
        "Swojej podróży nie zaczniesz z gołymi rękami"

        if pc.cash == 50:
            "Po ukończeniu szkolenia w Gildii Handlowej zostałeś:"
            menu (nvl=True):
                "Handlarzem medycznym":
                    python:
                        pc.wis += 2
                        pc.infamy -= 2
                        pc.job = "medic"
                    jump intro_2_1
                "Handlarzem skórami i innymi materiałami":
                    python:
                        pc.job = "idk"
                    jump intro_2_1
                "Handlarzem bronią":
                    python:
                        pc.infamy += 4
                        pc.job = "weapon"
                    jump intro_2_1
        elif pc.cash == 120:
            "Na misję zostałeś wysłany jako:"
            menu (nvl=True):
                "Handlarz ziołami i medykamentami":
                    python:
                        pc.wis += 2
                        pc.infamy -= 2
                        pc.job = "medic"
                    jump intro_2_2
                "Handlarz skórami zwierzęcymi":
                    python:
                        pc.job = "idk"
                    jump intro_2_2
                "Handlarz bronią":
                    python:
                        pc.infamy += 4
                        pc.job = "weapon"
                    jump intro_2_2
        elif pc.cash == 18:
            "Dzięki ciężkiej pracy w wiosce udało ci się zgromadzić dość towarów aby rozpocząć jako: "
            menu (nvl=True):
                "Wędrowny zielarz":
                    python:
                        pc.wis += 3
                        pc.infamy -= 2
                        pc.job = "medic"
                    jump intro_2_3
                "Sprzedawca skór":
                    python:
                        pc.job = "idk"
                    jump intro_2_3
                "Handlarz bronią":
                    python:
                        pc.infamy += 4
                        pc.job = "weapon"
                    jump intro_2_3

    label intro_2_1:
        nvl clear
        if pc.job == "medic":

            python:
                inventory.append(b_knife)
                inventory.append(lysvik_tea)
                inventory.append(herbs1)
                inventory.append(medical_herbs)


            "Bycie handlarzem leków, ziół i mikstur wymagało od ciebie lat studiowania ksiąg zielarzy i druidów."
            "Jest to ścieżka kariery, która wymaga od handlarza obszernej wiedzy na temat działania
             a często i wytwarzania wielu tajemniczych specyfików"
            "Mimo tego zdecydowałeś się na tą czasochłonną naukę."

        elif pc.job == "idk":

            python:
                inventory.append(h_knife)
                inventory.append(dried_meat2)
                inventory.append(wool)
                inventory.append(cow_hide)
                inventory.append(leather_strips)

            "Nigdy nie pałałeś miłością do nauk niezwiązanych z handlem, więc postanowiłeś skupić
             się na finansach i sprzedawać to czego potrzebuje każdy."
            "Futra, skóry, rzemienie, suszone mięso - to materiały które potrzebuje aboslutnie każdy absolutnie wszędzie."
            "Niezależnie od miejsca i czasu, można wszędzie je sprzedać i wszędzie uzupełnić zapasy."

        elif pc.job == "weapon":

            python:
                inventory.append(b_weapon)
                inventory.append(iron_ingot)
                inventory.append(chainmail)
                inventory.append(w_shield)
                inventory.append(iron_sword)



            "Na kontynencie od dziesiątek lat mają miejsce większe i mniejsze starcia pomiędzy
             mocarstwami i nie zapowiada się, by wojna szybko się skończyła."
            "Nie zależnie czy twoje towary trafią do żądnych zysku najemników czy do broniących
             się przed bandytami wieśniaków, na pewno nie będziesz narzekał na zawartość sakiewki."

        jump intro_3

    label intro_2_2:
        nvl clear
        if pc.job == "medic":

            python:
                inventory.append(n_knife)
                inventory.append(herbs2)
                inventory.append(herbs3)

            "Zaskoczyłeś zarówno swojego ojca jak i mentorów decydując się na najtrudniejszą z handlowych ścieżek."
            "Początkowo większość próbowała wybić ci z głowy spędzanie lat na studiowaniu działania i miejsc występowania leczniczych ziół,
            jednak w końcu ojciec docenił twój zapał do nauki i zrobił co w jego mocy by zapewnić ci najlepszych nauczycieli."
            "W końcu po latach studiowania nadszedł czas wyruszyć w drogę."

        elif pc.job == "idk":

            python:
                inventory.append(n_knife)
                inventory.append(dye)
                inventory.append(silk)
                inventory.append(dried_meat1)

            "Nigdy nie pałałeś miłością do nauk niezwiązanych z handlem, więc postanowiłeś skupić się na finansach
             i sprzedawać to czego potrzebuje każdy."
            "Futra, skóry, rzemienie, suszone mięso - to materiały które potrzebuje aboslutnie każdy absolutnie wszędzie."
            "Niezależnie od miejsca i czasu, można wszędzie je sprzedać i wszędzie uzupełnić zapasy."

        elif pc.job == "weapon":

            python:
                inventory.append(n_weapon)
                inventory.append(steel_ingot)
                inventory.append(g_shield)
                inventory.append(g_helmet)
                inventory.append(g_sword)
                inventory.append(longbow)
                inventory.append(arrows)


            "Na kontynencie od dziesiątek lat mają miejsce większe i mniejsze starcia pomiędzy
             mocarstwami i nie zapowiada się, by wojna szybko się skończyła."
            "Nie zależnie czy twoje towary trafią do żądnych zysku najemników czy
             do broniących się przed bandytami wieśniaków, na pewno nie będziesz narzekał na zawartość sakiewki."

        jump intro_3

    label intro_2_3:
        nvl clear
        if pc.job == "medic":

            # $inventory.append(["Nóż\n", "Korzonki na hemoroidy\n", "Zioła na nasenność\n", "Zdrowotne jagody\n", "Leśne zioła\n"])
            python:
                inventory.append(p_knife)
                inventory.append(herbs1)
                inventory.append(dried_berries)

            "Sprośród wszystkich zajęć, które mogłeś ćwiczyć na wsi najbardziej zaangażowały cię nauki zielarstwa u matki."
            "Wyruszałeś razem z nią do okolicznych lasów poznawać rosnące tam zioła, ich zastosowania i sposób obróbki."
            "Spędziłeś lata zapamiętując przekazywane z pokolenia na pokolenie zielarskie tajniki."
            "Kiedy matka uznała, że więcej już nie może cię nauczyć, rozpocząłeś przygotowania do swojej wyprawy"

        elif pc.job == "idk":

            python:
                inventory.append(p_knife)
                inventory.append(wool)
                inventory.append(dried_meat3)
                inventory.append(deer_pelt)


            "W czasie swojego dorastania starałeś się spróbować wszystkiego co mogła zaoferować ci wioska."
            "Nauczyłeś się jak oprawić skóry i futra, tworzyć rzemienie i sznury."
            "Tym co wypełniało cię chęcią do podróży były niesamowite historie opowiadane
            przez przyjezdnych zatrzymujących się w wiejskiej karczmie przed wjazdem do stolicy."
            "Załadowawszy wóz przedmiotami podarowanymi przez najbliżych i tymi wykonanymi własnoręcznie, rozpoczynasz swoją podróż."

        elif pc.job == "weapon":

            python:
                inventory.append(p_knife)
                inventory.append(p_weapon)
                inventory.append(iron_axe)
                inventory.append(w_shield)


            "Twoim głównym mentorem został wiejski kowal."
            "Podczas treningu dowiedziałeś, się, że tak na prawdę nie pochodzi on z twojej wioski."
            "Kiedyś pracował dla stacjonującego niedaleko garnizonu ale w końcu odszedł z wojska i zaszył się na okolicznej wsi."
            "Na kontynencie od dziesiątek lat mają miejsce większe i mniejsze starcia pomiędzy
             mocarstwami i nie zapowiada się, by wojna szybko się skończyła."
            nvl clear
            "Kowal zaproponował, że nauczy cię wykuwać broń ale przestrzegł cię przed idącymi z tym konsekwencjami."
            "Twoje towary trafią i do żądnych zysku najemników i do broniących się przed bandytami wieśniaków."
            "Niezależnie od tego, nie będziesz narzekać na pusty mieszek, zwłaszcza na pograniczach."

        jump intro_3


    label intro_3:
        nvl clear
        "Twoim głównym, prywatnym celem, który chcesz osiągnąć w podróży jest: "
        menu (nvl=True):
            "Zdobycie doświadczenia i zarobku":
                python:
                    pc.cha += 1
                    pc.cause = "money"
                jump intro_done
            "Spełnienie propozycji nie do odrzucenia...":
                python:
                    pc.wis += 1
                jump intro_spy
            "Pomocy innym" if pc.job != "weapon":
                python:
                    pc.infamy *= 2
                    pc.cause = "help"
                jump intro_done


    nvl clear

    label intro_done:
        nvl clear
        jump day1
