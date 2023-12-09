# archivo: main.py
import modules.sensorVentanaSala as sensor_ventana
import modules.sensorVentanaHabitacion as sensor_ventana_habitacion
import modules.sensorPuerta as sensor_puerta
import modules.sensorGas as sensor_gas
import modules.sensorIncendio as sensor_incendio
import modules.enviarMensaje as envio_correos

# Definir los pines para cada sensor
pines_sensor_ventana = (10, 11)
pines_sensor_ventana_habitacion = (12, 13)
pines_sensor_puerta = (14, 15)
pines_sensor_gas = (16, 17)
pines_sensor_incendio = (18, 19)

def verificar_sensor_ventana():
    if sensor_ventana.detectar(*pines_sensor_ventana):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de ventana', 'La ventana de la sala está abierta.')

def verificar_sensor_ventana_habitacion():
    if sensor_ventana_habitacion.detectar(*pines_sensor_ventana_habitacion):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de ventana habitación', 'La ventana de la habitación está abierta.')

def verificar_sensor_puerta():
    if sensor_puerta.detectar(*pines_sensor_puerta):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de puerta', 'La puerta está abierta.')

def verificar_sensor_gas():
    if sensor_gas.detectar(*pines_sensor_gas):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de gas', 'Se detectó gas.')

def verificar_sensor_incendio():
    if sensor_incendio.detectar(*pines_sensor_incendio):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de incendio', 'Se detectó un incendio.')

while True:
    verificar_sensor_ventana()
    verificar_sensor_ventana_habitacion()
    verificar_sensor_puerta()
    verificar_sensor_gas()
    verificar_sensor_incendio()