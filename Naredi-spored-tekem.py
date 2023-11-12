# V Pythonu je nepisano pravilo, da je dolžina vrstice manj kot 80 znakov. Če
# je daljša, jo je treba razdeliti. 79 znakov je do tukaj -------------------->
# To velja tako za kode kot tudi za komentarje.

# Za več informacij o slogu kode: `pip install flake8`. Nato v terminalu poženi
# `flake8 pot/do/datoteke/ime_datoteke.py` in terminal bo izpisal opozorila o
# nepravilnem slogu kode.

# Za hitrejše popravljanje sloga kode: `pip install autopep8`. Nato v terminalu
# poženi `autopep8 --in-place pot/do/datoteke/ime_datoteke.py` in datoteka bo
# popravljena.

# CILJ KODE: imamo seznam ekip ter hočemo sestaviti urnik tekem. Ekipe igrajo
# vsaka z vsako, enkrat doma, drugič v gosteh.

# OPOMBA: kodo se poganja v terminal, tako da oznacimo željeno (sicer se požene
# vrstica v kateri se nahaja kursor) + shift + enter

import random


def ekipe(n):
    """
    Komentar funkcije se piše tukaj. Tako lahko uporabnik izve kaj funkcija
    počne, ko z miško postavi kazalec na ime funkcije.

    Funkcija vrne seznam ekip, ki ga sestavlja n ekip. Ekipe so poimenovane z
    zaporednimi števili od 1 do n.
    """
    return list(range(1, n + 1))


def razpored(seznam):
    """
    Generira seznam vseh možnih tekem med ekipami v seznamu.
    """
    s = []
    for i in range(len(seznam)):
        for j in range(len(seznam)):
            if (seznam[i], seznam[j]) not in s and \
                    (seznam[j], seznam[i]) not in s:
                s.append((seznam[i], seznam[j]))
                s.append((seznam[j], seznam[i]))
    return s


def izbrisi_iste(seznam):
    """
    Izbrisemo tekme, ko igra ekipa proti sebi
    """
    s = []
    for i in seznam:
        if i[1] == i[0]:
            next
        else:
            s.append(i)
    return s


def končen_razpored(seznam, stevilo_dni):
    # cilj je imeti znotraj seznama s nove sezname, ki ponazarjajo dneve
    s = []

    # v range daš število dni na voljo (za 16 ekip je blo tu 30 cifra, saj
    # igrajo 30 dni)
    for i in range(stevilo_dni):
        s.append([])

    vse = set()
    dosedanje_tekme = set()
    for dan in s:
        ekipe_v_dnevu = set()
        for tekma in seznam:
            if tekma[0] in ekipe_v_dnevu or tekma[1] in ekipe_v_dnevu:
                vse.add(tekma)
            elif tekma not in dosedanje_tekme:
                dan.append(tekma)
                vse.add(tekma)
                dosedanje_tekme.add(tekma)
                ekipe_v_dnevu.add(tekma[0])
                ekipe_v_dnevu.add(tekma[1])
            else:
                vse.add(tekma)
        ekipe_v_dnevu = set()

    # ker matematično ni možno narediti takega urnika, nekatere tekme
    # izostanejo. Odigrali jih bomo kasneje.

    neodigrane = []
    for i in vse:  # najdemo pa jih v zadnjem seznamu seznama
        if i not in dosedanje_tekme:
            neodigrane.append(i)

    s.append(neodigrane)

    return s


def premesaj(a, ekipe):
    """
    S to funkcijo sem probal resiti problem, da ekipa na koncu ne igra enkrat v
    gosteh enkrat doma, temveč lahko večkrat zapored igra doma ali v gosteh.

    Cilj te funkcije naj bi bil, da vrne tak seznam tekem, da v osnovi vsaka
    ekipa enkrat igra doma, drugic pa v gosteh, izmenično.

    Ne dela kot bi morala.
    """
    indeks = True
    for i in ekipe:
        for tekma in a:
            if i not in tekma:
                continue
            elif indeks is True:
                if tekma.index(i) == 1:
                    indeks = 0
                elif tekma.index(i) == 0:
                    indeks = 1
            elif i in tekma and indeks == tekma.index(i):
                a.append(a.pop(a.index(tekma)))  # fukni ga na konec
            elif i in tekma and indeks != tekma.index(i):
                indeks = tekma.index(i)
    return a

# kar niso funkcije, vedno napišemo v main, da se ne poganjajo, če iz te
# datoteke importamo funkcije


if __name__ == '__main__':  # koda od tu naprej se požene le, če poženemo
                            # ta script. Ne bi se pa pognala, če ga
                            #uvozimo in pozenemo v drugem script-u.

    # 6 ekip vsaka igra 5-krat doma, 5-krat u gosteh
    # ekipe sem poimenoval kot stevilke zaradi manj pisanja

    ekipe_6 = ekipe(6)
    ekipe_16 = ekipe(16)
    ekipe_7 = ekipe(7)

    # OPOMBA: (1,2)..... 1 igra doma, 2 v gosteh
    #         (2,1)......ravno obratno

    a = izbrisi_iste(razpored(ekipe_6))  # vidimo da je tekm 30 v tem primeru
    b = izbrisi_iste(razpored(ekipe_16))
    c = izbrisi_iste(razpored(ekipe_7))

    # premesamo da ne igrajo ekipe 2-krat zapored en dan za drugim, saj je tako
    # prej narejen seznam
    random.shuffle(a)
    random.shuffle(b)
    random.shuffle(c)
    # =========================================================================

    # a
    # k = premesaj(a,ekipe)
    # k

    # b
    # g = premesaj(b, ekipe_16)
    # g

    # =========================================================================
    # bliznjica:  - zakomentiramo tako, da oznacimo + ctrl k + ctrl c
    #             - odkomentiramo tako, da oznacimo + ctrl k + ctrl u
    # =========================================================================

    stevilo_tekem1 = len(a)
    stevilo_tekem2 = len(b)
    stevilo_tekem3 = len(c)

    # primer za 16 ekip: recimo da imamo na voljo 30 dni, torej bo vsak dan
    # len(a)/30 tekem, in se ravno izzide (sicer moremo vzeti drugo število
    # dni)

    # primer za 6 ekip: tekem je 30, vsaka ekipa igra 10 tekem, recimo da imamo
    # na voljo 10 dni, torej bo vsak dan len(a)/10 tekem, in se ravno izide
    # vsak dan tri tekme

    stevilo_dni1 = 10
    stevilo_dni2 = 30
    stevilo_dni3 = 14

    dnevno_stevilo_tekem1 = len(a) / stevilo_dni1
    dnevno_stevilo_tekem2 = len(b) / stevilo_dni2
    dnevno_stevilo_tekem3 = len(c) / stevilo_dni3

    # razdelimo a na 30 enakih kosov

    # imamo 30 dni in 240 tekem, 8 tekem vsak dan, ena ekipa bo igrala 15*2
    # tekem skupno (proti vsaki drugi ekipi enkrat doma in enkrat v gosteh),
    # torej vsak dan eno

    # _____________________________________________________
    prvi = končen_razpored(a, stevilo_dni1)
    prvi

    len(prvi) == 11   # more biti true
    prvi[10]  # to so še neodigrane tekme

    # preverimo če je tekem res pravo število
    stevilo = 0
    for i in prvi:
        for j in i:
            stevilo += 1

    stevilo  # mora biti 30 ane
    # _________________________________________________
    drugi = končen_razpored(b, stevilo_dni2)
    drugi

    len(drugi) == 31  # more biti true
    drugi[30]  # to so še neodigrane tekme

    # preverimo če je tekem res pravo število
    stevilo = 0
    for i in drugi:
        for j in i:
            stevilo += 1

    stevilo  # more biti 240
    # _________________________________________
    tretji = končen_razpored(c, stevilo_dni3)
    tretji

    len(tretji) == 15  # more biti true
    tretji[14]  # to so še neodigrane tekme

    # preverimo če je tekem res pravo število
    stevilo = 0
    for i in tretji:
        for j in i:
            stevilo += 1

    stevilo  # more biti 42 ane

    # =============================================================================

    # OPOMBA:
    # ker sta a in b premešana randomly, ekipe lahko igrajo več tekem zapored
    # doma ali v gosteh. Zgoraj sem posušal narediti funkcijo, ki bi uredila
    # tako da bi izmenično enkrat igrali doma drugič ne, neuspešno.
    # Recimo, da nam random zaenkrat zadošča

    # OPOMBA: Ce je pa ekip liho, samo dodas eno imaginarno ekipo in potem
    # odstranis vse njene tekme na koncu

    # mogoče gre skozi tudi za liho število ekip, je treba sprobat (zgleda da
    # deluje, kot kaže primer s sedmimi ekipami),treba je le pazitit koliko dni
    # hočemo da igrajo ter koliko bo tekem v dnevu.

    # Tudi ce hoces potem da mas umes kdaj za ekipe dneve kjer nimajo tekm
    # usake toliko, dodas pa vec imaginarnih ekip in jih iz outputa brišes z
    # novo funkcijo
