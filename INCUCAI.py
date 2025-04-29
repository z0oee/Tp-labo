class INCUCAI:


    def __init__(self):
        self.receptores = []
        self.donantes = []
        self.Centros_de_salud = []

    def asignar_lista(self):
        numero=int(input("A que lista quiere agregar?\n1- Lista Receptores\n2-Lista donantes"))
        if numero == 1:
            for i in self.receptores:
                return