class Donante:


    def __init__(self, fecha_fall, hora_fall, fecha_abla, hora_abla):
        self.fecha_fall= fecha_fall
        self.hora_fall = hora_fall
        self.fecha_abla = fecha_abla # va a ser el mismo que reciba la clase organos, la fecha y hora
        self.hora_abla = hora_abla
        self.organos= [] #lista de organos a donar
