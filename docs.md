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


## 1. **Issues**

Las **issues** son herramientas de gestión de tareas, bugs y mejoras dentro de un repositorio de GitHub.  
Pueden ser:
- **Errores (bugs)** que hay que arreglar
- **Nuevas funcionalidades** que alguien propone
- **Tareas** por hacer
- **Dudas** o discusiones técnicas

Cada issue es como un “ticket” donde se puede:
- Describir el problema o tarea
- Comentar entre los miembros del equipo
- Asignar responsables
- Etiquetar (labels) para organizar
- Relacionar con commits y pull requests

**Ejemplo:**  
“Hay un error cuando sumo números negativos” → Issue donde se explica y se puede hacer seguimiento hasta resolverlo.

---

## 2. **Actions**

**GitHub Actions** es una plataforma de automatización.  
Permite definir flujos de trabajo (workflows) automáticos para tu proyecto, como:
- Ejecutar tests cada vez que haces un push
- Hacer el build de tu aplicación
- Desplegar automáticamente
- Analizar el código en busca de errores

Todo esto se configura con archivos `.yml` en `.github/workflows/`.  
Ejemplo: Cada vez que subes código, GitHub Actions puede correr tus tests y avisarte si algo falla.

---

## 3. **CODEOWNERS**

El archivo `CODEOWNERS` (usualmente en la raíz del repo o en `.github/`) sirve para definir **quién es responsable de cada parte del código**.

- Puedes asignar personas o equipos a ciertos archivos o carpetas.
- Si alguien hace un Pull Request que modifica esos archivos, los CODEOWNERS serán notificados y deberán revisarlo obligatoriamente.

**Ejemplo de CODEOWNERS:**
```
# El equipo backend es dueño de la carpeta backend/
backend/ @grupo-backend

# Juan es dueño del archivo Dockerfile
Dockerfile @juanperez
```

---

## 4. **Dependabot**

**Dependabot** es una herramienta integrada en GitHub para **mantener actualizadas las dependencias** de tu proyecto (por seguridad y estabilidad).

- Automáticamente revisa tus archivos de dependencias (por ejemplo, `requirements.txt` en Python, `package.json` en JavaScript, etc.).
- Si encuentra una versión nueva o una vulnerabilidad, crea un **Pull Request automático** para actualizar esa dependencia.
- Así siempre tienes tu código más seguro y actualizado, ¡con mínimo esfuerzo!

---


## Licencia
MIT

---

> Proyecto para el taller de *Integración y Entrega Continua* – [Z0SO](https://github.com/Z0SO)
