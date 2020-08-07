



class Fabrica():
    def __init__(self, serie_inceput = 0, bucati =0) -> int:
        self.serie_inceput = serie_inceput
        self.bucati = bucati

    def serii_dreapta(self):
        if self.serie_inceput % 2 == 0:
            return (self.serie_inceput, self.bucati)

    def serii_stanga(self):
        if self.serie_inceput % 2 != 0:
            return (self.serie_inceput, self.bucati)

    def __iter__(self):
        return (self.serii, self.bucati)


class Loturi(Fabrica):
    def __init__(self, lot) -> int:
        self.lot = lot
        self.lot = (self.serie_inceput, self.bucati)
        dreapta = 0
        stanga = 0
        for i in self.lot:
            if self.serie_inceput % 2 == 0:
                dreapta.append(i)
            else:
                stanga.append(i)


loturi = Loturi()
fab = Fabrica.Loturi(314,90)






