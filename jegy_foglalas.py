from datetime import datetime, timedelta

from main import legitarsasag

class JegyFoglalas:
    def __init__(self, utas_nev, jarat, datum, ulohely):
        self.foglalas_azonosito = self._generate_id()
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum
        self.ulohely = ulohely
        self.statusz = "Foglalt"
        self.foglalas_ideje = datetime.now()

    def _generate_id(self):
        return f"FOG-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def torles(self):
        self.statusz = "Törölve"

    def modositas(self, uj_ulohely):
        self.ulohely = uj_ulohely

    def get_foglalas_info(self):
        return {
            "azonosito": self.foglalas_azonosito,
            "utas": self.utas_nev,
            "jarat": self.jarat.jaratszam,
            "celallomas": self.jarat.celallomas,
            "datum": self.datum,
            "ulohely": self.ulohely,
            "statusz": self.statusz
        }

# 1. metódus: Foglalás lemondása
def foglalas_torles(foglalas):
    if foglalas_ellenorzes(foglalas):
        foglalas.torles()
        print(f"A(z) {foglalas.utas_nev} által {foglalas.datum}-ra foglalt jegy törölve.")
    else:
        print("A foglalás már érvénytelen vagy nem létezik.")

# 2. metódus: Foglalások listázása
def foglalasok_listazasa(legitarsasag):
    print("Aktuális foglalások:")
    for foglalas in legitarsasag.foglalasok:
        print(foglalas.get_foglalas_info())

# 3. metódus: Foglalás érvényességének ellenőrzése
def foglalas_ellenorzes(foglalas):
    jarat = foglalas.jarat
    if jarat in legitarsasag.jaratok and foglalas.datum >= datetime.now().date() + timedelta(days=1):
        return True
    else:
        return False

# 5. metódus: Jegy foglalása
def jegy_foglalas(legitarsasag):
    utas_nev = input("Kérem, adja meg az utas nevét: ")
    print("Elérhető járatok:")
    for jarat in legitarsasag.jaratok:
        print(f"{jarat.jaratszam} - {jarat.celallomas} ({jarat.get_vegso_ar()} Ft)")
    jaratszam = input("Kérem, adja meg a kiválasztott járat számát: ")
    jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jaratszam), None)
    if jarat:
        foglalas_datum = input("Kérem, adja meg a foglalás dátumát (YYYY-MM-DD): ")
        ulohely = input("Kérem, adja meg a kívánt ülőhelyet: ")
        if foglalas_ellenorzes(JegyFoglalas(utas_nev, jarat, foglalas_datum, ulohely)):
            foglalas = JegyFoglalas(utas_nev, jarat, foglalas_datum, ulohely)
            legitarsasag.foglalasok.append(foglalas)
            print(f"A(z) {utas_nev} részére {jarat.celallomas} járatra {foglalas_datum}-ra, {ulohely} ülőhelyre sikeresen lefoglaltuk a jegyet.")
        else:
            print("A megadott időpontra vagy járatra nem lehet foglalni.")
            jegy_foglalas(legitarsasag)
    else:
        print("Érvénytelen járatszám. Kérem, próbálja újra.")
        jegy_foglalas(legitarsasag)

# 6. metódus: Foglalás lemondása
def foglalasok_torles(legitarsasag):
    foglalasok_listazasa(legitarsasag)
    foglalas_id = input("Adja meg a törölni kívánt foglalás azonosítóját: ")
    for foglalas in legitarsasag.foglalasok:
        if foglalas.foglalas_azonosito == foglalas_id:
            foglalas_torles(foglalas)
            return
    print("Nem található ilyen foglalás.")

# 7. metódus: Foglalások listázása
def foglalasok_listazasa(legitarsasag):
    print("Aktuális foglalások:")
    for foglalas in legitarsasag.foglalasok:
        print(foglalas.get_foglalas_info())