from flask import Flask, request
import requests
import itertools
import time

app = Flask(__name__)

# Lista de servidores Flask disponibles
servers = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

# Verifica qué servidores están activos
alive_servers = []
for s in servers:
    try:
        requests.get(s, timeout=1)
        alive_servers.append(s)
    except:
        print(f"[⚠️] Servidor {s} no responde. Será omitido del balanceo.")

if not alive_servers:
    raise Exception("❌ No hay servidores activos disponibles.")

# Ciclo round-robin de los servidores activos
server_cycle = itertools.cycle(alive_servers)

@app.route('/', methods=['GET', 'POST'])
def balance():
    target = next(server_cycle)
    start = time.time()
    try:
        response = requests.get(target)
        elapsed = time.time() - start
        return (
            f"🔀 Balanceador Flask activo\n"
            f"➡️ Servidor destino: {target}\n"
            f"⏱ Tiempo de respuesta: {elapsed:.3f}s\n"
            f"📦 Respuesta: {response.text}\n"
        )
    except Exception as e:
        return f"❌ Error al contactar {target}: {e}"

if __name__ == '__main__':
    app.run(port=5000)

