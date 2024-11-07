from jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, megye):
        super().__init__(jaratszam, celallomas, jegyar)
        self.megye = megye
        self.kedvezmeny = 0.2  # 20% kedvezmény

    def get_vegso_ar(self):
        return self.jegyar * (1 - self.kedvezmeny)
