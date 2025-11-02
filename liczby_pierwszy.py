def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def liczby_pierwsze_do(n):
    liczby_pierwsze = []
    for i in range(2, n + 1):
        if czy_pierwsza(i):
            liczby_pierwsze.append(i)
    return liczby_pierwsze

def main():
    n = int(input("Podaj zakres (do jakiej liczby chcesz znaleźć liczby pierwsze): "))
    wynik = liczby_pierwsze_do(n)
    print(f"Liczby pierwsze do {n}:")
    print(wynik)

# Wywołanie programu
main()
