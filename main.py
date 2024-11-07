from legi_tarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from jegy_foglalas import JegyFoglalas

# Létrehozzuk a légitársaságot
legitarsasag = LegiTarsasag("Magyar Légitársaság")

# Létrehozunk egy belföldi járatot
belfoldi = BelfoldiJarat("HU123", "Debrecen", 15000, "Hajdú-Bihar")

# Létrehozunk egy nemzetközi járatot
nemzetkozi = NemzetkoziJarat("INT456", "Bécs", 45000, "Ausztria")

# Hozzáadjuk a járatokat a légitársasághoz
legitarsasag.jarat_hozzaadasa(belfoldi)
legitarsasag.jarat_hozzaadasa(nemzetkozi)

# Foglalás létrehozása
foglalas = JegyFoglalas("Kiss János", belfoldi, "2024-05-01", "12A")

# Információk kiírása
print(f"Belföldi jegy ára: {belfoldi.get_vegso_ar()} Ft")
print(f"Nemzetközi jegy ára: {nemzetkozi.get_vegso_ar()} Ft")
print(foglalas.get_foglalas_info())