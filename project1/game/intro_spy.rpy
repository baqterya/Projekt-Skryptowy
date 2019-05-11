label intro_spy:
    nvl clear
    stop music fadeout 3.0
    scene black
    with Pause(3.5)
    scene bg inn1
    with fade

    play music "inn.mp3" fadein 3.0


    n "W pierwszym dniu swojej podróży zatrzymałeś się w przydrożnej karczmie aby spędzić pierwszą noc poza rodzinną okolicą.{p}

     Mimo tłoku udało Ci się znaleźć wolne miejsce, gdzie teraz w spokoju dopijasz kufel miejscowego piwa."

    n "Nagle, jak z podziemii wyrasta przed tobą niewielka postać w płaszczu."

    n "Bierze wolne krzesło ze stolika obok i przysiada się do ciebie ściągając kaptur z głowy."

    n "Postać okazała się być starym gnomem o bujnej ale białej jak śnieg czuprynie."

    n "Nieznajomy poprawił jeszcze raz odrobinę zbyt duże krzesło i zwrócił na ciebie swoje duże, przenikliwe, zielone oczy."

    n "Po czym odzywa się niskim, zachrypiałym głosem."

    if t_background == "burgher":
        jump spy_burgher
    elif t_background == "noble":
        jump spy_noble
    elif t_background == "peasant":
        jump spy_peasant

    label spy_burgher:
        g "Co sprowadza takiego młodzieńca do zapyziałej przydrożnej karczmy, eh?"

        menu:
            "Podróżuję ze zlecenia Gildii Kupieckiej.":
                pass
            "Jestem w podróży do moich rodzinnych stron.":
                jump spy_bluff
            "Nie twój interes.":
                jump spy_rude

        g "Tak się składa, że ja podobnie.{p} Liczyłem na spotkanie kolegi po fachu ale nie spodziewałem się takiego nowicjusza."

        n "Gnom rozgląda się szybko po karczmie i wraca wzrokiem do ciebie, uśmiechając się spod gęstego wąsa równie białego co jego włosy."

        g "Tak się składa, że poszukuję partnera, do pewnego zadania, które mi zlecono."

        g "A ty wyglądasz na kogoś kto się będzie nadawał!"

        g "Powiedz mi chłopcze, jaki jest cel twojej wędrówki."

        menu:
            "Urdinas.":
                pass
            "Helvegen, niewielkie miasto na pograniczu.":
                jump spy_bluff
            "Nie twoja sprawa, ciekawski starcze.":
                jump spy_rude

        g "Ooo, to długa podróż, tak się składa."

        g "Ale jestem gotów dobrze zapłacić za pomoc."

        n "Twój rozmówca wyciągna spod płaszcza mieszek złota."

        g "To zaliczka."

        if t_background != "peasant":
            g "W ciągu trasy będziesz prowadził dziennik.{p}Kilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."
        else:
            g "Zapamiętuj dobrze wszysto co spotka cię na trasie.{p}Kilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."

        g "Każdy z nich przyniesie dodatkową zapłatę."

        n "Gnom przesuwa mieszek na twoją stronę stołu i zaczyna podnosić się z krzesła."

        $ cash += 34

        g "Miło robi się z tobą interesy."

        n "Starzec uśmiecha się ponownie spod wąsa, zeskakuje z krzesła, zakłada kaptur na głowę i wychodzi z karczmy"

        jump intro_done


        label spy_bluff:
            n "Próbujesz zbyć swojego rozmówcę najbardziej wiarygodnym kłamstwem jakie przyszło ci do głowy."


            g "Uwierz mi, że w moim fachu lubimy załatwiać sprawy w przyjacielskiej atmosferze."

            if t_background == "noble":
                g "Więc jeśli nie chcesz, żeby wpływy twojego ojca w Gildii Kupieckiej zaczęły niespodziewanie i niepokojąco maleć..."
            elif t_background == "burgher":
                g "Jeśli źle będziemy się dogadywać, to może zdarzyć się tak, że ani ty, ani twój ojciec nie będziecie już mile widziani w Gildii..."
            elif t_background == "peasant":
                g "Doszły mnie słuchy, że twój ojciec w młodości zdezerterował z armii. Normalnie nikt nie dociekałby tak starej sprawy, ale..."

            g "Mam nadzieję, że się zrozumieliśmy."

            if t_background != "peasant":
                g "W ciągu trasy będziesz prowadził dziennik.{p}Kilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."
            else:
                g "Zapamiętuj dobrze wszysto co spotka cię na trasie.{p}Kilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."

            g "Jeśli sobie załużysz, otrzymasz sowitą zapłatę."

            g "I nie polecam próbować już więcej takich sztuczek."

            jump intro_done

        label spy_rude:
            n "Po twarzy twojego rozmówcy widać, że nie spodobała mu się twoja odpowiedź..."

            g "Obawiam się, że źle oceniasz swoją sytuację."

            g "Uwierz mi, że w moim fachu lubimy załatwiać sprawy w przyjacielskiej atmosferze."

            g "Ale nie będę wachał się przed odwdzięczeniem za niemiłe słowa."

            n "Gnom zeskakuje z krzesła i przybliża się do twojej twarzy wbijając w ciebie swój prznikliwy wzrok."

            if t_background == "noble":
                g "Gildii Handlowej nie brakuje inwestorów, więc nikt nie poczuje straty jednego z nich..."

                g "Jeśli dobrze się rozumiemy, to zrobisz dokładnie to co ci powiem."

            elif t_background == "burgher":
                g "Jeszcze jedna taka odzywka a zapewniam cię, że nie będziesz miał dokąd wracać w Lysvik."

                g "A teraz lepiej słuchaj uważnie co musisz zrobić."

            elif t_background == "peasant":
                g "Jeżeli nie chcesz aby jakiś przykry wypadek przydażył się w twojej rodzinnej mieścinie, to radzę słuchać uważnie."

            if t_background != "peasant":
                g "W ciągu trasy będziesz prowadził dziennik.{p}Kilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."
            else:
                g "Zapamiętuj dobrze wszysto co spotka cię na trasie.{p} ilka razy w ciągu całej trasy spotka się z tobą ktoś z moich podwładnych."

            g "I nie polecam próbować już więcej takich sztuczek."

            jump intro_done
