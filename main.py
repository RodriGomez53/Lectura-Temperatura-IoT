#A continuación se muestra el código a
#ejecutar en la tarjeta Raspberry Pi Pico W,
#Es importante guardarlo en la tarjeta con el
#nombre "main.py", de lo contrario no se ejecutará
#al conectarla a una fuente de alimentación externa
import network
import urequests
import time
from machine import ADC, Pin

# Configuración Wi-Fi
ssid = "Tu_SSID"
password = "Tu_Contraseña"

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "TU_API_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Configuración del sensor LM35 (conectado al pin GP26 / ADC0)
sensor = ADC(Pin(26))

# Función para conectar a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    
    print("Conectado! Dirección IP:", wlan.ifconfig()[0])

# Función para leer la temperatura del LM35
def leer_temperatura():
    lectura = sensor.read_u16()  # Lectura ADC de 16 bits
    voltaje = (lectura / 65535.0) * 3.3  # Convertir a voltaje (0-3.3V)
    temperatura = voltaje * 100  # LM35: 10mV/°C -> 1V = 100°C
    return temperatura

# Función para enviar datos a ThingSpeak
def enviar_a_thingspeak(temperatura):
    try:
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={temperatura}"
        respuesta = urequests.get(url)
        print(f"Enviado a ThingSpeak: {temperatura}°C - Respuesta: {respuesta.text}")
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)

# Conectar a Wi-Fi
conectar_wifi()

# Bucle principal: Enviar datos cada 3 minutos (180 segundos)
while True:
    temperatura = leer_temperatura()
    print(f"Temperatura actual: {temperatura:.2f}°C")
    enviar_a_thingspeak(temperatura)
    time.sleep(180)  # Espera 3 minutos antes de la próxima lectura
