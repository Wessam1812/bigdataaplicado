# Proyecto Big Data - SmartManuTech

# Para instalar las dependencias necesarias:
pip install -r requirements.txt

1. Ejecutar Docker para levantar los servicios (tener abierto docker)
docker-compose up -d
2. Ejecutar el productor
python producer.py
3. Ejecutar el consumidor 
python consumer.py
4. Ejecutar la API:
uvicorn main:app --reload
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
