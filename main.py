from legi_tarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from jegy_foglalas import JegyFoglalas, foglalas_torles, foglalasok_listazasa, foglalas_ellenorzes, jegy_foglalas, foglalasok_torles
from datetime import datetime, timedelta

# Létrehozzuk a légitársaságot
legitarsasag = LegiTarsasag("Magyar Légitársaság")

# Létrehozzunk 3 járatot
belfoldi1 = BelfoldiJarat("HU123", "Debrecen", 15000, "Hajdú-Bihar")
belfoldi2 = BelfoldiJarat("HU456", "Szeged", 17000, "Csongrád-Csanád")
nemzetkozi = NemzetkoziJarat("INT789", "Bécs", 45000, "Ausztria")

# Hozzáadjuk a járatokat a légitársasághoz
legitarsasag.jarat_hozzaadasa(belfoldi1)
legitarsasag.jarat_hozzaadasa(belfoldi2)
legitarsasag.jarat_hozzaadasa(nemzetkozi)

# Létrehozunk 6 foglalást
foglalas1 = JegyFoglalas("Kiss János", belfoldi1, "2024-05-01", "12A")
foglalas2 = JegyFoglalas("Kovács Mária", nemzetkozi, "2024-06-15", "7C")
foglalas3 = JegyFoglalas("Nagy Péter", belfoldi2, "2024-07-20", "4E")
foglalas4 = JegyFoglalas("Szabó Ildikó", belfoldi1, "2024-08-10", "9B")
foglalas5 = JegyFoglalas("Horváth Gábor", nemzetkozi, "2024-09-01", "2D")
foglalas6 = JegyFoglalas("Tóth Katalin", belfoldi2, "2024-10-05", "15F")

# 4. metódus: Egyszerű felhasználói felület
def menu():
    print("Üdvözöljük a Magyar Légitársaság foglalási rendszerében!")
    print("Kérem, válasszon a következő opciók közül:")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Válasszon (1-4): ")

    if valasztas == "1":
        jegy_foglalas(legitarsasag)
    elif valasztas == "2":
        foglalasok_torles(legitarsasag)
    elif valasztas == "3":
        foglalasok_listazasa(legitarsasag)
    elif valasztas == "4":
        print("Viszontlátásra!")
    else:
        print("Érvénytelen választás. Kérem, próbálja újra.")
        menu()

# 8. metódus: Kezdeti adat betöltése
legitarsasag.foglalasok = [foglalas1, foglalas2, foglalas3, foglalas4, foglalas5, foglalas6]

# Felhasználói felület indítása
menu()