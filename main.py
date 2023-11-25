import RPi.GPIO as GPIO
import time

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)
# Definir el pin del LED
pin_led = 17

# Configurar el pin del LED como salida
GPIO.setup(pin_led, GPIO.OUT)

try:
    # Encender el LED
    print("Encendiendo el LED...")
    GPIO.output(pin_led, GPIO.HIGH)

    # Esperar 2 segundos
    time.sleep(2)

    # Apagar el LED
    print("Apagando el LED...")
    GPIO.output(pin_led, GPIO.LOW)

except KeyboardInterrupt:
    # Limpiar pines y recursos al presionar Ctrl+C
    GPIO.cleanup()