# Creati o clasa numita Triunghi.
#  - obiectele create cu aceasta clasa au 3 variabile de instanta are reprezinta unghiurile triungiului si au valoarea
# initiala de 60 de grade
#  - clasa are o metoda numita modifica_unghi si primeste ca argumente unghiul si numarul de grade cu care trebuie
#  modificat ca si int
# - deoarece suma ungiurilor intr-un triungi trebe sa fie 180 grade metoda de modificare a unui unghiului trebuie sa
# ajusteze celelalte doua variabile reprezentand ungiuri cu valori egale astfel ca suma celor 3 variabile sa ramana 180
# - Daca modificarea ungiului are ca rezultat un unghi in afara intervalului deschis (0-180) metoda va ridica exceptia
# AttributeError

class Triunghi():
    def __init__(self, a=60.0, b=60.0, c=60.0):
        self.a = a
        self.b = b
        self.c = c

    def modifica_unghi(self, unghi, modificare):

        if modificare not in range(0, 121):
            raise AttributeError("Valoarea nu este in range!")
        else:

            if unghi == my_tri.a:
                self.a = self.a + modificare
                self.b = self.b - modificare / 2
                self.c = self.c - modificare / 2

            elif unghi == my_tri.b:
                self.b = self.b + modificare
                self.a = self.a - modificare / 2
                self.c = self.c - modificare / 2

            else:
                self.c = self.c + modificare
                self.a = self.a - modificare / 2
                self.b = self.b - modificare / 2
            return self.a, self.b, self.c


my_tri = Triunghi()
print(my_tri.modifica_unghi(my_tri.a, 45))
