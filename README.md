# 🌍 Proyecto: Balanceador de Carga para Servicios Web Distribuidos

**Autor:** Samuel Escobar  
**Sistema operativo:** Ubuntu
**Lenguaje:** Python 3  
**Framework:** Flask + NGINX 
**Algoritmo de balanceo:** Round-Robin

---

## 📘 Descripción
Este proyecto implementa un **balanceador de carga HTTP** que distribuye solicitudes entre tres microservicios simulados, Combina **NGINX como proxy frontal** y **Flask como balanceador inteligente**.  
Cada microservicio responde con un mensaje distinto, y el balanceador reparte las peticiones de forma cíclica (Round-Robin).


---

## 🧩 Componentes

| Componente | Puerto | Descripción |
|-------------|---------|--------------|
| Servidor 1 | 5001 | Microservicio Flask 1 |
| Servidor 2 | 5002 | Microservicio Flask 2 |
| Servidor 3 | 5003 | Microservicio Flask 3 |
| Balanceador Flask | 5000 | Implementa algoritmo Round-Robin |
| Proxy NGINX | 8080 | Entrada frontal del sistema |
