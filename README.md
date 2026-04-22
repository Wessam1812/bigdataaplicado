# Proyecto Big Data - SmartManuTech

1.Para instalar las dependencias necesarias:
pip install -r requirements.txt
2. Ejecutar Docker para levantar los servicios (tener abierto docker)
docker-compose up -d
3. Ejecutar el productor
python producer.py
4. Ejecutar el consumidor 
python consumer.py
5. Ejecutar la API:
uvicorn main:app --reload
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
