from datetime import datetime


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