## ¿Qué es el archivo `.yml`, el directorio `.github` y `workflows`?

### **a) `.github/`**

Este directorio en tu repo es especial para GitHub. Todo lo que pongas ahí son configuraciones relacionadas con cómo GitHub interactúa con tu proyecto:
- **Actions** (CI/CD): workflows automáticos para testing, build, deploy, etc.
- **Templates**: para issues, pull requests, etc.
- **Dependabot**, **CODEOWNERS**, etc.

### **b) `.github/workflows/`**

Dentro de `.github`, la carpeta `workflows` contiene los archivos de configuración de workflows de **GitHub Actions**.  
Cada archivo `.yml` (o `.yaml`) es un workflow independiente que define una secuencia de pasos automáticos para tu repo, por ejemplo:
- Correr tests.
- Hacer builds.
- Hacer deploy.
- Analizar el código, etc.

### **c) El archivo `.yml` (ejemplo: `ci.yml`)**

Es un archivo en formato YAML donde describes el pipeline de CI/CD.  
En él defines:
- **Cuándo** se dispara el workflow (por ejemplo, al hacer `push` a `master`).
- **En qué sistema** corre (por ejemplo, Ubuntu).
- **Qué pasos** ejecutar (instalar dependencias, correr tests, build de Docker, etc.).

**Ejemplo explicado paso a paso:**

```yaml
name: CI/CD Pipeline   # Nombre descriptivo

on:
  push:
    branches: [ "master" ]       # Corre cuando haces push a master
  pull_request:
    branches: [ "master" ]       # O cuando hay un PR hacia master

jobs:
  build-test:                    # Nombre del job (puedes tener varios jobs)
    runs-on: ubuntu-latest       # Usa una máquina virtual Ubuntu

    steps:
    - name: Checkout código
      uses: actions/checkout@v4  # Baja tu código del repo

    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"   # Elige la versión de Python

    - name: Instalar dependencias
      run: pip install -r requirements.txt   # Instala tus dependencias

    - name: Ejecutar tests
      run: pytest test_app.py                # Corre los tests

    - name: Construir imagen Docker
      run: docker build -t ic-demo-python .  # Build de tu imagen docker

    - name: Ejecutar contenedor Docker (opcional)
      run: docker run --rm ic-demo-python    # Ejecuta la app en Docker
```

**Resumen:**  
- GitHub Actions te permite automatizar tareas (como testing, deploy, análisis de código, etc.) en tu repo.
- Todo workflow se define en un `.yml` dentro de `.github/workflows/`.
- El `.yml` es súper flexible: puedes tener muchos workflows distintos y cada uno con múltiples jobs y pasos.


---

## Licencia

MIT

---

> Proyecto para el taller de *Integración y Entrega Continua* – [Z0SO](https://github.com/Z0SO)
