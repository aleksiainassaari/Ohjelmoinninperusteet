"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    print(varaus)

    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(varausId))
    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()
print("Varausnumero: 123")
print("Varaaja: Anna Virtanen")
print("Päivämäärä: 31.10.2025")
print("Aloitusaika: 10.00")
print("Tuntimäärä: 2")
print("Tuntihinta: 19.95 €")
print("Kokonaishinta: 39.9 €")
print("Maksettu: Kyllä")
print("Kohde: Kokoustila A")
print("Puhelin: 0401234567")
print("Sähköposti: anna.virtanen@example.com")

tuntimaara = 2
tuntihinta = 19.95
kokonaishinta = tuntimaara * tuntihinta
print(f"Kokonaishinta: {kokonaishinta:.2f} €")
maksettu = True  # tai False
print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
hinta = 19.95
suomalainen_muoto = f"{hinta:.2f}".replace(".", ",")
print(suomalainen_muoto)
tuntimaara = 2
aloitusaika = 10.00
loppumisaika = aloitusaika + tuntimaara
print(f"Loppumisaika: {loppumisaika:.2f}")

print("Varausnumero: 124")
print("Varaaja: Aleksi Ainassaari")
print("Päivämäärä: 31.10.2025")
print("Aloitusaika: 12.00")
print("Tuntimäärä: 2")
print("Tuntihinta: 19.95 €")
print("Kokonaishinta: 39.9 €")
print("Maksettu: Kyllä")
print("Kohde: Kokoustila A")
print("Puhelin: 044254888")
print("Sähköposti: Aleksi.Ainassaari@example.com")
tuntimaara = 2
aloitusaika = 12.00
loppumisaika = aloitusaika + tuntimaara
print(f"Loppumisaika: {loppumisaika:.2f}")
hinta = 19.95
suomalainen_muoto = f"{hinta:.2f}".replace(".", ",")
print(suomalainen_muoto)

