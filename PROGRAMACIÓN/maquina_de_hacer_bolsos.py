class MaquinaDeHacerBolsos():
    def __init__(self, material, color, tamano):
        self.__material = material
        self.__color = color
        self.__tamano = tamano
        self.__estado = False
        self.__piezas_cortadas = False
        self.__piezas_cocidas = False

    def get_material(self):
        return self.__material
    def set_material(self, material):
        self.__material = material
    
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_tamano(self):
        return self.__tamano
    def set_tamano(self, tamano):
        self.__tamano = tamano

    def encender(self):
        self.__estado = True
        return 'Máquina encendida.'

    def cortar_tela(self):
        if not self.__estado:
            return ('Error: La máquina está apagada. Debes encenderla primero.')
        if not self.__piezas_cortadas:
            self.__piezas_cortadas = True
            return (f'Cortando la tela de tipo {self.__material}, color {self.__color} y tamaño {self.__tamano}.')
        else:
            return ('Las piezas ya están cortadas.')

    def coser_piezas(self):
        if self.__piezas_cortadas and not self.__piezas_cocidas:
            self.__piezas_cocidas = True
            return ('Cosiendo las piezas del bolso.')
        elif not self.__piezas_cortadas:
            return ('Primero necesitas cortar la tela.')
        else:
            return ('Las piezas ya están cocidas.')

    def __str__(self):
        if self.__estado and self.__piezas_cocidas:
            return 'Bolso terminado.'
        return 'Proceso incompleto.'    
    
if __name__ == '__main__':
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    print(maquina.cortar_tela())
    print(maquina.encender())
    print(maquina.cortar_tela())
    print(maquina.coser_piezas())
    print(maquina)