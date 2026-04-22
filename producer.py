import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generar_datos():
    return {
        "temperatura": random.randint(40, 100),
        "vibracion": random.randint(10, 90),
        "velocidad": random.randint(50, 120),
        "energia": random.randint(80, 300),
        "timestamp": time.time()
    }

print("📡 Enviando datos IoT...")

while True:
    data = generar_datos()
    producer.send('iot-data', data)
    print("Enviado:", data)
    time.sleep(2)