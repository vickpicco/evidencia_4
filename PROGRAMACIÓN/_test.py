from maquina_de_hacer_bolsos import MaquinaDeHacerBolsos
import pytest

def test_encender():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    assert maquina.encender() == 'Máquina encendida.'

def test_cortar_tela():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    maquina.encender()
    assert maquina.cortar_tela() == f'Cortando la tela de tipo {maquina.get_material()}, color {maquina.get_color()} y tamaño {maquina.get_tamano()}.'
    assert maquina.get_material() == 'cuero'
    assert maquina.get_color() == 'negro'
    assert maquina.get_tamano() == 'mediano'

def test_cortar_tela_sin_encender():
    maquina = MaquinaDeHacerBolsos("cuero", "negro", "mediano")
    maquina.cortar_tela()
    assert maquina.cortar_tela() == 'Error: La máquina está apagada. Debes encenderla primero.'

def test_coser_piezas():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    maquina.encender()
    maquina.cortar_tela()
    assert maquina.coser_piezas() == 'Cosiendo las piezas del bolso.'

def test_coser_piezas_sin_cortar_tela():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    maquina.encender()
    assert maquina.coser_piezas() == 'Primero necesitas cortar la tela.'

def test_proceso_incompleto():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    maquina.encender()
    maquina.cortar_tela()
    assert maquina.__str__() == 'Proceso incompleto.'

def test_bolso_terminado():
    maquina = MaquinaDeHacerBolsos('cuero', 'negro', 'mediano')
    maquina.encender()
    maquina.cortar_tela()
    maquina.coser_piezas()
    assert maquina.__str__() == 'Bolso terminado.'


if __name__ == '__main__':
    pytest.main()