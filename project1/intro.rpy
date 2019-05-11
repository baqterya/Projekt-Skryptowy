define narrator = nvl_narrator

label intro:
    "Rozpoczynasz swoją przygodę jako ludzki kupiec z leżącej na północy Federacji Lyvsik"

    "Wychowałeś się w: "
    menu (nvl=True):
        "Mieszczańskiej rodzinie ze stolicy":
            python:
                t_background = "burgher"
                cash = 50
                t_int += 1
                t_cha += 1
            jump intro_1

        "Pomniejszym rodzie szlacheckim":
            python:
                t_background = "noble"
                cash = 120
                t_int += 1
                t_inf -= 2
            jump intro_1

        "Ubogiej rodzinie z podgrodzia":
            python:
                t_background = "peasant"
                cash = 18
                t_int += 2
                t_cha -= 2
            jump intro_1


    label intro_1:
        nvl clear

        if t_background == "burgher":
            "Większość swojego życia spędziłeś w Lysvik - stolicy Federacji ludzi, krasnoludów i gnomów zamieszkujących północ Arrionu."
            "Tam właśnie wychowałeś się w rodzinie jednego z licznych Lysvickich kupców. Od kiedy pamiętasz podziwiałeś przedsiębiorczość"
            "ojca i szybko poszedłeś w jego ślady. Widząc w tobie potencjał, wysłał cię na nauki u swojego starego mistrza."
            nvl clear
            "W końcu po latach nauki zostałeś oficjalnym członkiem gildii handlowej. Teraz czeka cię twoje pierwsze poważne zadanie:"
            "Musisz udać się w długą podróż do Wolnego Miasta Urdinas."

        elif t_background == "noble":
            "Wychowałeś się w wysokich sferach Lysvik - stolicy Federacji ludzi, krasnoludów i gnomów zamieszkujących północ Arrionu."
            "Chociaż twój ród nie należy do najbardziej wpływowych politycznie to twój ojciec jest poważnym udziałowcem gildii handlowej."
            "Od kiedy pamiętasz zawsze zależało mu na budowie prestiżu rodu więc zapewnił ci, jako swojemu następcy, najlepszą możliwą edukację."
            "Zarówno on jak i gildia handlowa pokładają w tobie nadzieję, bo to od ciebie będzie zależeć wasza przyszła współpraca."
            nvl clear
            "Po ukończeniu szkolenia zostałeś wybrany do swojej pierwszej ważnej misji. "
            "Masz za zadanie jak najszybciej dotrzeć do Urdinas - Miasta Gildii aby
             spotkać się z przedstawicielami Jedwabnego Liścia - najbardziej wpływowej gildii handlowej na całym kontynencie."

        elif t_background == "peasant":
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

        if cash == 50:
            "Po ukończeniu szkolenia w Gildii Handlowej zostałeś:"
            menu (nvl=True):
                "Handlarzem medycznym":
                    python:
                        t_int += 2
                        t_inf -= 2
                        t_job = "medic"
                    jump intro_2_1
                "Handlarzem skórami i innymi materiałami":
                    python:
                        t_job = "idk"
                    jump intro_2_1
                "Handlarzem bronią":
                    python:
                        t_inf += 4
                        t_job = "weapon"
                    jump intro_2_1
        elif cash == 120:
            "Na misję zostałeś wysłany jako:"
            menu (nvl=True):
                "Handlarz ziołami i medykamentami":
                    python:
                        t_int += 2
                        t_inf -= 2
                        t_job = "medic"
                    jump intro_2_2
                "Handlarz skórami zwierzęcymi":
                    python:
                        t_job = "idk"
                    jump intro_2_2
                "Handlarz bronią":
                    python:
                        t_inf += 4
                        t_job = "weapon"
                    jump intro_2_2
        elif cash == 18:
            "Dzięki ciężkiej pracy w wiosce udało ci się zgromadzić dość towarów aby rozpocząć jako: "
            menu (nvl=True):
                "Wędrowny zielarz":
                    python:
                        t_int += 3
                        t_inf -= 2
                        t_job = "medic"
                    jump intro_2_3
                "Sprzedawca skór":
                    python:
                        t_job = "idk"
                    jump intro_2_3
                "Handlarz bronią":
                    python:
                        t_inf += 4
                        t_job = "weapon"
                    jump intro_2_3

    label intro_2_1:
        nvl clear
        if t_job == "medic":

            "Bycie handlarzem leków, ziół i mikstur wymagało od ciebie lat studiowania ksiąg zielarzy i druidów."
            "Jest to ścieżka kariery, która wymaga od handlarza obszernej wiedzy na temat działania
             a często i wytwarzania wielu tajemniczych specyfików"
            "Mimo tego zdecydowałeś się na tą czasochłonną naukę."

        elif t_job == "idk":

            "Nigdy nie pałałeś miłością do nauk niezwiązanych z handlem, więc postanowiłeś skupić
             się na finansach i sprzedawać to czego potrzebuje każdy."
            "Futra, skóry, rzemienie, suszone mięso - to materiały które potrzebuje aboslutnie każdy absolutnie wszędzie."
            "Niezależnie od miejsca i czasu, można wszędzie je sprzedać i wszędzie uzupełnić zapasy."

        elif t_job == "weapon":

            "Na kontynencie od dziesiątek lat mają miejsce większe i mniejsze starcia pomiędzy
             mocarstwami i nie zapowiada się, by wojna szybko się skończyła."
            "Nie zależnie czy twoje towary trafią do żądnych zysku najemników czy do broniących
             się przed bandytami wieśniaków, na pewno nie będziesz narzekał na zawartość sakiewki."

        jump intro_3

    label intro_2_2:
        nvl clear
        if t_job == "medic":

            "Zaskoczyłeś zarówno swojego ojca jak i mentorów decydując się na najtrudniejszą z handlowych ścieżek."
            "Początkowo większość próbowała wybić ci z głowy spędzanie lat na studiowaniu działania i miejsc występowania leczniczych ziół,
            jednak w końcu ojciec docenił twój zapał do nauki i zrobił co w jego mocy by zapewnić ci najlepszych nauczycieli."
            "W końcu po latach studiowania nadszedł czas wyruszyć w drogę."

        elif t_job == "idk":

            "Nigdy nie pałałeś miłością do nauk niezwiązanych z handlem, więc postanowiłeś skupić się na finansach
             i sprzedawać to czego potrzebuje każdy."
            "Futra, skóry, rzemienie, suszone mięso - to materiały które potrzebuje aboslutnie każdy absolutnie wszędzie."
            "Niezależnie od miejsca i czasu, można wszędzie je sprzedać i wszędzie uzupełnić zapasy."

        elif t_job == "weapon":

            "Na kontynencie od dziesiątek lat mają miejsce większe i mniejsze starcia pomiędzy
             mocarstwami i nie zapowiada się, by wojna szybko się skończyła."
            "Nie zależnie czy twoje towary trafią do żądnych zysku najemników czy
             do broniących się przed bandytami wieśniaków, na pewno nie będziesz narzekał na zawartość sakiewki."

        jump intro_3

    label intro_2_3:
        nvl clear
        if t_job == "medic":

            "Sprośród wszystkich zajęć, które mogłeś ćwiczyć na wsi najbardziej zaangażowały cię nauki zielarstwa u matki."
            "Wyruszałeś razem z nią do okolicznych lasów poznawać rosnące tam zioła, ich zastosowania i sposób obróbki."
            "Spędziłeś lata zapamiętując przekazywane z pokolenia na pokolenie zielarskie tajniki."
            "Kiedy matka uznała, że więcej już nie może cię nauczyć, rozpocząłeś przygotowania do swojej wyprawy"

        elif t_job == "idk":

            "W czasie swojego dorastania starałeś się spróbować wszystkiego co mogła zaoferować ci wioska."
            "Nauczyłeś się jak oprawić skóry i futra, tworzyć rzemienie i sznury."
            "Tym co wypełniało cię chęcią do podróży były niesamowite historie opowiadane
            przez przyjezdnych zatrzymujących się w wiejskiej karczmie przed wjazdem do stolicy."
            "Załadowawszy wóz przedmiotami podarowanymi przez najbliżych i tymi wykonanymi własnoręcznie, rozpoczynasz swoją podróż."

        elif t_job == "weapon":

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
                    t_cha += 1
                    t_cause = "money"
                jump intro_done
            "Spełnienie propozycji nie do odrzucenia...":
                python:
                    t_int += 1
                jump intro_spy
            "Pomocy innym" if t_job != "weapon":
                python:
                    t_inf *= 2
                    t_cause = "help"
                jump intro_done


    nvl clear

    label intro_done:
        nvl clear
        jump day1
