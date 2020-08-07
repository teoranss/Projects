"""
Module for saving car series
"""
class CarFactory():
    """
    Class for creating car series and lots
    """
    serii = []
    loturi = []

    def __init__(self, serie_start, numar_bucati) -> int:
        self.serie_start = serie_start
        self.numar_bucati = numar_bucati
        self.__calcul_serii()
        self.__calcul_loturi()

    def __calcul_serii(self):
        self.serii = list(range(self.serie_start, self.serie_start + self.numar_bucati))

    def __calcul_loturi(self):
        lot_start = self.serie_start // 20
        lot_stop = (self.serie_start + self.numar_bucati) // 20
        lot_start += 1 if self.serie_start % 20 else 0
        lot_stop += 1 if (self.serie_start + self.numar_bucati) % 20 else 0
        self.loturi = list(range(lot_start, lot_stop + 1))

    def serii_stanga(self):
        lista_serii_stanga = []
        for i in self.serii:
            if i % 2:
                lista_serii_stanga.append(i)
        return lista_serii_stanga

    def serii_dreapta(self):
        lista_serii_dreapta = []
        for i in self.serii:
            if not i % 2:
                lista_serii_dreapta.append(i)
        return lista_serii_dreapta

    def __iter__(self):
        return CarFactoryIterator(self.serii)


class CarFactoryIterator():

    def __init__(self, serii):
        self.serii = serii

    def __iter__(self):
        pass

    def __next__(self):
        if not self.serii:
            raise StopIteration
        return self.serii.pop(0)


car_factory = CarFactory(314, 90)

with open("Serii.txt", mode='x') as file:
    for car in car_factory:
        file.write(str(car) + '\n')

# print(car_factory.serii)
# print(len(car_factory.serii))
# print(car_factory.loturi)
# print(car_factory.serii_stanga())
# print(car_factory.serii_dreapta())
