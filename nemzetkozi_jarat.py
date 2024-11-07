from jarat import Jarat


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, orszag):
        super().__init__(jaratszam, celallomas, jegyar)
        self.orszag = orszag
        self.biztositas = 5000  # extra biztosítás

    def get_vegso_ar(self):
        return self.jegyar + self.biztositas