
# ic-demo-python

Este proyecto es un ejemplo simple para demostrar la integración y entrega continua (CI/CD) usando **GitHub Actions**, **Docker** y **Python** para un taller académico.

## Descripción

- El código consiste en una función que cuenta la cantidad de vocales en un texto en Python.
- Se incluyen pruebas automatizadas con pytest.
- El despliegue se realiza en un contenedor Docker.

## Estructura del proyecto

```
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

## CI/CD

![CI/CD](https://github.com/Z0SO/ic-demo-pyhton/actions/workflows/ci.yml/badge.svg?branch=master)

- Al hacer `push` o `pull request` a la rama `master`, se ejecuta el workflow de GitHub Actions que:
  1. Instala dependencias.
  2. Corre los tests.
  3. Si los tests pasan, construye la imagen Docker.
  4. Ejecuta el contenedor para verificar el funcionamiento.

## Uso local

### Requisitos

- Python 3.11+
- Docker
- Pip

### Instalación

```bash
pip install -r requirements.txt
```

### Ejecutar aplicación

```bash
python app.py
```

### Ejecutar tests

```bash
pytest test_app.py
```

### Ejecutar con Docker

Construir imagen:
```bash
docker build -t ic-demo-python .
```

Ejecutar contenedor:
```bash
docker run --rm ic-demo-python
```

## Licencia

MIT

---

> Proyecto para el taller de *Integración y Entrega Continua* – [Z0SO](https://github.com/Z0SO)
