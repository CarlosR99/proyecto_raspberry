import RPi.GPIO as GPIO
import time 
import proyecto_raspberry.modules.sensor_Incendio as  mensaje   #CORREGIR COMOSE DEBE LLAMAR LA FUNCION 


def detectar_incendio():
    led_pin = 11
    pulsador_encendido_pin = 12
    pulsador_apagado_pin = 18

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)
    GPIO.setup(led_pin, GPIO.OUT)

    led_encendido = False

    

    try:
        while True:
            if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                while GPIO.input(pulsador_apagado_pin) == GPIO.LOW:
                    pass
                GPIO.output(led_pin, GPIO.LOW)
                led_encendido = False
                time.sleep(0.1)

                # Llamar a la función de notificación
                envio_correos(destinatario, asunto, cuerpo)

    except KeyboardInterrupt:
        GPIO.cleanup() 