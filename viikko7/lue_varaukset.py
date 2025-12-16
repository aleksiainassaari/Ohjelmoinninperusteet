# Copyright (c) 2025 Aleksi Ainassaari
# License: MIT

#käytän tässä tehtävässä sanakirjoja
# sanakirjat ovat selkeämpiä kuin paljaat listat, koska ne nimeävät merkityksen (avaimet), kun taas listat luottavat indeksien muistamiseen. 

from __future__ import annotations
from datetime import datetime, date, time
from typing import List, Dict, Any


def muunna_varaustiedot(varaus_lista: List[str]) -> Dict[str, Any]:
    

    
    raw_hinta = str(varaus_lista[7]).replace(",", ".")
    raw_bool = str(varaus_lista[8]).strip().lower()
    vahvistettu = raw_bool in {"true", "1", "yes", "y", "on"}   

    return {
    "id": int(varaus_lista[0]),
    "nimi": varaus_lista[1],
    "sahkoposti": varaus_lista[2],
    "puhelin": varaus_lista[3],
    "paivamaara": datetime.strptime(varaus_lista[4], "%Y-%m-%d").date(),
    "kellonaika": datetime.strptime(varaus_lista[5], "%H:%M").time(),
    "kesto": int(varaus_lista[6]),
    "hinta": float(raw_hinta),
    "vahvistettu": vahvistettu,
    "tila": varaus_lista[9],
    "luotu": datetime.strptime(varaus_lista[10], "%Y-%m-%d %H:%M:%S")
    }

def hae_varaukset(varaustiedosto: str) -> List[Dict[str, Any]]:

    varaukset: List[Dict[str, Any]] = []

    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            r = rivi.strip()
            if not r or r.startswith("#"):
                continue
            osat = r.split("|")
            if len(osat) != 11:
                continue
            varaukset.append(muunna_varaustiedot(osat))
    return varaukset


def vahvistetut_varaukset(varaukset:List[Dict[str, Any]]) -> None:
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            print(f"- {varaus['nimi']}, {varaus['tila']}, "
                  f"{varaus['paivamaara'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}")

    print()
def pitkat_varaukset(varaukset: List[Dict[str, Any]]) -> None:
    for varaus in varaukset:
        if varaus["kesto"] >= 3:
            print(f"- {varaus['nimi']}, {varaus['paivamaara'].strftime('%d.%m.%Y')}"
                  f" klo {varaus['kellonaika'].strftime('%H.%M')}, kesto {varaus['kesto']} h, {varaus['tila']}")
    print()

def varausten_vahvistusstatus(varaukset: List[Dict[str, Any]]) -> None:
    for varaus in varaukset:
        status = "vahvistettu" if varaus["vahvistettu"] else "EI vahvistettu"
        print(f"- {varaus['nimi']},{status}, "
              f"{varaus['paivamaara'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}")    

    print()

def varausten_lkm(varaukset: List[Dict[str, Any]]) -> None:
    vahvistetut = sum(1 for v in varaukset if v["vahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")

    print()



def varausten_kokonaistulot(varaukset: List[Dict[str, Any]]) -> None:
    tulot =sum(v["kesto"] * v["hinta"] for v in varaukset if v["vahvistettu"])
    print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")

    print()
    

def main() -> None:
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)

    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

    
varaukset = hae_varaukset("varaukset.txt")
print(type(varaukset[0]))  # pitäisi tulostaa: <class 'dict'>


if __name__ == "__main__":
    main()


