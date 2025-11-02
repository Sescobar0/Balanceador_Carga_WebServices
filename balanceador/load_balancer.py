from flask import Flask, request
import requests
import itertools
import time

app = Flask(__name__)

# Lista de servidores disponibles
servers = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

# Generador cíclico para el algoritmo Round-Robin
server_cycle = itertools.cycle(servers)

@app.route('/', methods=['GET', 'POST'])
def balance():
    # Obtiene el siguiente servidor de la lista
    target = next(server_cycle)

    start = time.time()
    try:
        # Reenvía la solicitud al servidor seleccionado
        response = requests.get(target)
        elapsed = time.time() - start
        return f"""
        Petición enviada a: {target}  
        Tiempo de respuesta: {elapsed:.3f} segundos  
        Respuesta: {response.text}
        """
    except Exception as e:
        return f"Error al contactar {target}: {e}"

if __name__ == '__main__':
    app.run(port=5000)
