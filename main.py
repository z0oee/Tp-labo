from Centros_de_salud import Centro_de_salud
from INCUCAI import INCUCAI
from Donante import Donante
from Organos import Organos
from Paciente import Paciente
from Receptor import Receptor
from Vehiculos import Vehiculos

def main():
    paciente= Paciente("Zoe", 46821489, "6/11/2005", "F", 1126485713, "0+", "Favaloro", "Donante")

    paciente.datos_pacientes()


if __name__ == "__main__":
    main()