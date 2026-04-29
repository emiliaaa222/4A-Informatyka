def horner(w, x):
    wynik = 0

    for i in w:
        wynik = wynik * x + i

    return wynik


# dane (wielomian: 2x^2 + 3x + 1)
wsp = [2, 3, 1]
x = 2

wynik = horner(wsp, x)

print("Wynik:", wynik)
