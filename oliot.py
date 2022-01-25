

# Mo

# LUOKKIEN MÄÄRITTELY

# Määritellään lainjluokka, joka ei peri mitään
from asyncio.proactor_events import _ProactorBasePipeTransport


class Lainaaja:

    # Uuden olion luonti (constructor)
    def __init__(self, opiskelikanumero, etunimi, sukunimi):
        # self viittaa tulevaan olioon, jonka nimi ei vielä tiedossa
        self.opiskelijanumero = opiskelikanumero
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Olion metodit -> mitä olio osaa tehdä
    def tulosta_opiskelijanumero(self):
        print("opiskelijanumero on:", self.opiskelijanumero)

    def tulosta_kaikki_tiedot(self):
        print('Opiskelijanumero:', self.opiskelijanumero,'\n','etunimi',self.etunimi,'\n''sukunimi', self.sukunimi)


# VARSINAINEN OHJELMA

# Luodaan lainaaja-olio Lainaaja-luokasta

lainaaja1 = Lainaaja(123456, 'Mauri', 'Hutikka')

# Testataan lainaaja1-oliota
print('Lainaaja1 on', lainaaja1.etunimi, lainaaja1.sukunimi)

lainaaja1.tulosta_opiskelijanumero()
lainaaja1.tulosta_kaikki_tiedot()