def szybkie_potegowanie(podstawa, wykladnik):
    if wykladnik < 0:
        podstawa = 1 / podstawa
        wykladnik = -wykladnik
    
    wynik = 1
    while wykladnik > 0:
        if wykladnik % 2 == 1:
            wynik *= podstawa
        podstawa *= podstawa
        wykladnik //= 2
    return wynik



# --- Przykład działania ---
a = 2
n = 4
print(f"{a}^{n} = {szybkie_potegowanie(a, n)}")