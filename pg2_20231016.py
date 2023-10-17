import random
from gpiozero import LED, Button
import time
import psutil

Verde = LED(17)
Rojo = LED(18)
Azul = LED(19)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)

    if cpu_percent <= 10:
        print("Verde On, Amarillo Off, Rojo Off")

    if cpu_percent > 10 and cpu_percent <= 20:
        print("Verde Off, Amarillo ON, Rojo Off")
    if cpu_percent > 20:

        print("Verde Off, Amarillo Off, Rojo parpadeando")

# 2do Programa Lectura de Temperatura


temperaturas = []

while True:

    temperatura_simulada = random.uniform(20, 30)
    temperaturas.append(temperatura_simulada)

    if len(temperaturas) > 10:
        temperaturas.pop(0)

    promedio_temperatura = sum(temperaturas) / len(temperaturas)
    print(f'Promedio de temperatura: {promedio_temperatura:.2f}°C')

    time.sleep(10)
