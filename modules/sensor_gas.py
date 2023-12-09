import RPi.GPIO as GPIO  # Importa la biblioteca para controlar los pines
import time  # Importa la biblioteca para controlar el tiempo
import modulos.envio_correos as envio_correos # se sugiere usar la rupta para nuestro proyecto...

def detectar_gas():
    led_pin = 11  # Define el pin GPIO para el LED
    pulsador_encendido_pin = 13  # Define el pin GPIO para el pulsador de encendido
    pulsador_apagado_pin = 18  # Define el pin GPIO para el pulsador de apagado

    GPIO.setwarnings(False)  # Desactiva las advertencias
    GPIO.setmode(GPIO.BOARD)  # Configura los pines GPIO en modo BOARD
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)  # Configura el pulsador de encendido como e6y6567uo8klllll.l....ntrada
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)  # Configura el pulsador de apagado como entrada
    GPIO.setup(led_pin, GPIO.OUT)  # Configura el LED como salida

    led_encendido = False  # Inicializa el LED en estado apagado

    try:
        while True:  # Bucle infinito
            if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH and not led_encendido:  # Si el pulsador de encendido está activado y el LED está apagado
                GPIO.output(led_pin, GPIO.HIGH)  # Enciende el LED
                led_encendido = True  # Actualiza el estado del LED a encendido
                while GPIO.input(pulsador_apagado_pin) == GPIO.LOW:  # Mientras el pulsador de apagado esté desactivado
                    pass  # No hace nada
                GPIO.output(led_pin, GPIO.LOW)  # Apaga el LED
                led_encendido = False  # Actualiza el estado del LED a apagado
                time.sleep(0.1)  # Espera un décimo de segundo

    except KeyboardInterrupt:  
        GPIO.cleanup()  # Limpia los pines GPIO
