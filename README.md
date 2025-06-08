# Guía rápida: Configuración de entorno virtual y Flask

Guía paso a paso para crear un entorno virtual en Python e instalar Flask y pandas para ejecutar la aplicación en Flask.

---

## 1. Crear un entorno virtual (venv)

Abre la terminal y ejecuta:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` con el entorno virtual.

---

## 2. Activar el entorno virtual

### En Windows

```bash
venv\Scripts\activate
```

### En macOS/Linux

```bash
source venv/bin/activate
```

El prompt de la terminal ahora inicia con `(venv)`.

---

## 3. Instalar Flask y pandas

Con el entorno virtual activado, instalar los paquetes necesarios:

```bash
pip install flask pandas
```

Se puede crear un archivo `requirements.txt` para registrar las dependencias:

```bash
pip freeze > requirements.txt
```

---

## 4. Ejecutar (activar) Flask

Para iniciar Flask:

```bash
flask run
```


## 5. Detener (desactivar) Flask

Para detener el servidor Flask, presionar `Ctrl+C` en la terminal donde está corriendo.

---

## 6. Desactivar el entorno virtual


```bash
deactivate
```

---


