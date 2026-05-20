def sortowanie(t):
    if len(t) <= 1:
        return t

    m = len(t) // 2

    lewa = sortowanie(t[:m])
    prawa = sortowanie(t[m:])

    wynik = []
    i = j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1

    wynik += lewa[i:]
    wynik += prawa[j:]

    return wynik


tab = [4, 1, 7, 2, 9]

print(sortowanie(tab))
