from kafka import KafkaConsumer
import json
from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch("http://localhost:9200")

consumer = KafkaConsumer(
    'iot-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📥 Procesando datos...")

def detectar_alertas(data):
    alertas = []

    if data["temperatura"] > 80:
        alertas.append("Alta temperatura")

    if data["vibracion"] > 70:
        alertas.append("Vibración excesiva")

    if data["velocidad"] < 60:
        alertas.append("Bajo rendimiento")

    if data["energia"] > 250:
        alertas.append("Consumo elevado")

    if data["temperatura"] > 95 and data["vibracion"] > 80:
        alertas.append("Error crítico")

    return alertas

for message in consumer:
    data = message.value
    alertas = detectar_alertas(data)

    documento = {
        "data": data,
        "alertas": alertas,
        "timestamp": datetime.now()
    }

   
    es.index(index="iot_data", document=documento)

    if alertas:
        print("🚨 ALERTA:", alertas)
    else:
        print("✅ OK:", data)