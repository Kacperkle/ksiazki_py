import csv
import os

class Book:
    def __init__(self, nazwa, autor, rok, jest):
        self.nazwa = nazwa
        self.autor = autor
        self.rok = rok
        self.jest = jest

ksiazki = {}
def dodaj_ksiazke():
    nazwa = input("Podaj nazwę książki: ")
    autor = input("Podaj autora: ")
    while True:
        try:
            rok = int(input("Podaj rok wydania: "))
            ksiazki[nazwa] = Book(nazwa, autor, rok, True)
            print("Książka została dodana.")
            break
        except ValueError:
            print("Rok wydania musi być liczbą całkowitą!")
            continue

def wypozycz():
    wyp = input("Podaj książkę do wypożyczenia: ")
    if wyp in ksiazki and ksiazki[wyp].jest:
        ksiazki[wyp].jest = False
        print(f"Książka '{wyp}' została wypożyczona.")
    else:
        print("Książka nie jest dostępna.")

def zwruc():
    zw = input("Podaj książkę do zwrotu: ")
    if zw in ksiazki and not ksiazki[zw].jest:
        ksiazki[zw].jest = True
        print(f"Książka '{zw}' została zwrócona.")
    else:
        print("Niepoprawna operacja.")

def wyswietl_ksiazki():
    dostepne_ksiazki = filter(lambda k: k.jest, ksiazki.values())
    print("\nDostępne książki:")
    print(f"{'Nazwa':<20} | {'Autor':<20} | Rok")
    print("-" * 50)
    for ksiazka in dostepne_ksiazki:
        print(f"{ksiazka.nazwa:<20} | {ksiazka.autor:<20} | {ksiazka.rok}")

def zapisz_do_csv():
    try:
        with open("ksiazki.csv", mode="w", newline='', encoding="utf-8") as plik:
            writer = csv.writer(plik)
            for ksiazka in ksiazki.values():
                writer.writerow([ksiazka.nazwa, ksiazka.autor, ksiazka.rok, ksiazka.jest])
    except Exception as e:
        print(f"Błąd zapisu: {e}")

def wczytaj_z_csv():
    if os.path.exists("ksiazki.csv"):
        try:
            with open("ksiazki.csv", mode="r", newline='', encoding="utf-8") as plik:
                reader = csv.reader(plik)
                for row in reader:
                    if len(row) == 4:
                        ksiazki[row[0]] = Book(row[0], row[1], int(row[2]), row[3] == 'True')
        except Exception as e:
            print(f"Błąd odczytu: {e}")

def main():
    wczytaj_z_csv()
    while True:
        print("\n1 - Dodaj książkę")
        print("2 - Wypożycz książkę")
        print("3 - Zwróć książkę")
        print("4 - Pokaż dostępne książki")
        print("5 - Zapisz do pliku")
        print("6 - Wczytaj z pliku")
        print("7 - Wyłącz")
        try:
            wybor = int(input("Wybierz opcję: "))
            print("")
        except ValueError:
            print("Musisz podać numer od 1 do 7.")
            continue

        if wybor == 1:
            dodaj_ksiazke()
        elif wybor == 2:
            wypozycz()
        elif wybor == 3:
            zwruc()
        elif wybor == 4:
            wyswietl_ksiazki()
        elif wybor == 5:
            zapisz_do_csv()
            print("Zapisano do pliku.")
        elif wybor == 6:
            wczytaj_z_csv()
        elif wybor == 7:
            zapisz_do_csv()
            print("Zakończono program.")
            break
        else:
            print("Niepoprawna opcja.")

if __name__ == "__main__":
    main()