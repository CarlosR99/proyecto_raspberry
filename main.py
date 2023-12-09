# archivo: main.py
import RPi.GPIO as GPIO
import modules.sensorVentanaSala as sensor_ventana
import modules.sensorVentanaHabitacion as sensor_ventana_habitacion
import modules.sensorPuerta as sensor_puerta
import modules.sensorGas as sensor_gas
import modules.sensorIncendio as sensor_incendio
import modules.enviarMensaje as envio_correos

# Definir los pines para cada sensor
pines_sensor_ventana = (7, 18)
pines_sensor_ventana_habitacion = (22, 18)
pines_sensor_puerta = (15, 18)
pines_sensor_gas = (13, 18)
pines_sensor_incendio = (12, 18)

# Definir el pin para el LED
pin_led = 11

def verificar_sensor_ventana():
    if sensor_ventana.detectar(*pines_sensor_ventana, pin_led):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de ventana', 'La ventana de la sala está abierta.')

def verificar_sensor_ventana_habitacion():
    if sensor_ventana_habitacion.detectar(*pines_sensor_ventana_habitacion, pin_led):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de ventana habitación', 'La ventana de la habitación está abierta.')

def verificar_sensor_puerta():
    if sensor_puerta.detectar(*pines_sensor_puerta, pin_led):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de puerta', 'La puerta está abierta.')

def verificar_sensor_gas():
    if sensor_gas.detectar(*pines_sensor_gas, pin_led):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de gas', 'Se detectó gas.')

def verificar_sensor_incendio():
    if sensor_incendio.detectar(*pines_sensor_incendio, pin_led):
        envio_correos.enviar('juan.jose.agudelo@correounivalle.edu.co', 'Alerta de incendio', 'Se detectó un incendio.')

while True:
    verificar_sensor_ventana()
    verificar_sensor_ventana_habitacion()
    verificar_sensor_puerta()
    verificar_sensor_gas()
    verificar_sensor_incendio()