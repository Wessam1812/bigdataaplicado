from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>SmartManuTech</title>
        </head>
        <body style="font-family:Arial; text-align:center; margin-top:50px;">
            <h1>SmartManuTech</h1>
            <p>Sistema de monitoreo Big Data en tiempo real</p>
            <a href="/docs">Ir a la API</a>
        </body>
    </html>
    """