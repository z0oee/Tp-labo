class Paciente:


    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, tipo_sangre, centro_salud, que_es):
        self.nombre = nombre
        self.DNI = DNI
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.telefono = telefono 
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud
        self.que_es = que_es #para ver si es receptor o donante 
        self.lista_pacientes=[]

    def agregar(self):
        print("Ingrese datos del receptor:")
        self.nombre = input("Ingrese nombre:")
        self.DNI = int(input("Ingrese DNI:"))
        self.fecha_nac = input("Ingrese fecha de nacimiento:")
        if super().asignar_lista() == 1:
            
    def datos_pacientes(self):
        print(f"El paciente es {self.nombre}\nDNI:{self.DNI}\nfecha de nacimiento:{self.fecha_nac}")
