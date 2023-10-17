from gpiozero import LED, Button
import time
import psutil

Verde=LED(17)
Rojo=LED(18)
Azul=LED(19)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    
    if cpu_percent<=10:
        Verde.on()
        Rojo.off()
        Azul.off()
    if cpu_percent>10 and cpu_percent<=20:
        Verde.off()
        Rojo.on()
        Azul.off()
    if cpu_percent>20:
        Verde.off()
        Rojo.off()
        Azul.on()

#2do Programa Lectura de Temperatura
import time
import random  


temperaturas = []

while True:

    temperatura_simulada = random.uniform(20, 30) 
    temperaturas.append(temperatura_simulada)


    if len(temperaturas) > 10:
        temperaturas.pop(0)


    promedio_temperatura = sum(temperaturas) / len(temperaturas)
    print(f'Promedio de temperatura: {promedio_temperatura:.2f}°C')


    time.sleep(10) 
