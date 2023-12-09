# archivo: sensor_puerta.py
import RPi.GPIO as GPIO

def detectar(pulsador_encendido_pin, pulsador_apagado_pin, pin_led):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)
    GPIO.setup(pin_led, GPIO.OUT)  # Configurar el pin del LED como salida

    while True:
        if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH:
            GPIO.output(pin_led, GPIO.HIGH)  # Encender el LED
            while GPIO.input(pulsador_apagado_pin) == GPIO.LOW:
                pass
            GPIO.output(pin_led, GPIO.LOW)  # Apagar el LED cuando la ventana se cierra
            return True