







from datetime import datetime, date


def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput int

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]