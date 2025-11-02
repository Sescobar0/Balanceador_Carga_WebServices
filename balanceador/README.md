# 🌍 Proyecto: Balanceador de Carga para Servicios Web Distribuidos

**Autor:** Samuel Escobar  
**Sistema operativo:** Ubuntu / Kali Linux  
**Lenguaje:** Python 3  
**Framework:** Flask  
**Algoritmo de balanceo:** Round-Robin

---

## 📘 Descripción
Este proyecto implementa un **balanceador de carga HTTP** que distribuye solicitudes entre tres microservicios simulados, desarrollados con Flask.  
Cada microservicio responde con un mensaje distinto, y el balanceador reparte las peticiones de forma cíclica (Round-Robin).

---

## ⚙️ Requisitos previos

Asegúrate de tener instaladas las siguientes herramientas:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
