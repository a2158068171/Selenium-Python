
# 🚀 Guía para Pruebas de Automatización con Selenium y Pytest-BDD

Este proyecto proporciona una solución de pruebas automatizadas utilizando **Selenium**, **Pytest** y **Pytest-BDD** con enfoque en arquitectura limpia mediante el patrón **Page Object Model**. Ideal para validar flujos funcionales en aplicaciones web de forma estructurada, legible y mantenible.

> 💡 El propósito principal es facilitar la implementación de pruebas automatizadas que sean escalables, reutilizables y fáciles de leer para testers y desarrolladores.

----------

## 🧰 Requisitos Previos

-   ✅ Python 3.6 o superior
    
-   ✅ Navegador **Google Chrome** instalado
    
-   ✅ **ChromeDriver** compatible con la versión de tu Chrome
    
-   ✅ Acceso a consola o terminal
    

----------

## ⚙️ Instalación

### 1. Crear un entorno virtual e instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
source venv/Scripts/activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias necesarias
pip install selenium pytest pytest-bdd allure-pytest

```

> 📦 También puedes crear un archivo `requirements.txt` con las dependencias y usar:  
> `pip install -r requirements.txt`

----------

## 📁 Estructura del Proyecto
###  Crear estructura de archivos
```bash
git clone https://github.com/a2158068171/Selenium-Python.git
cd Selenium-Python
```
Asegúrate de que tu estructura siga este patrón:

```
proyecto/
├── conftest.py                   # Configuraciones y fixtures globales
├── pytest.ini                    # Configuración de Pytest
├── features/                     # Archivos .feature para pruebas BDD
│   ├── register.feature
│   └── steps/
│       ├── __init__.py
│       └── test_register.py
├── pages/                        # Page Objects y acciones
│   ├── actions/
│   │   ├── __init__.py
│   │   ├── base_actions.py
│   │   └── register_actions.py
│   └── pages_objects/
│       ├── __init__.py
│       └── register.py

```

----------

## ⚙️ Configuración

### `pytest.ini` ya incluye:

-   ✅ Configuración para generar reportes con **Allure**
    
-   ⚠️ Ignorar advertencias de certificados HTTPS no verificados
    
-   💬 Salida de consola más legible
    
-   📁 Directorio base para archivos `.feature`
    
-   🏷️ Marcadores para ejecutar pruebas por prioridad (`@low`, `@medium`, `@high`)
    

----------

## 🧪 Ejecución de Pruebas

### Ejecutar todas las pruebas:

```bash
pytest

```

### Ejecutar pruebas por prioridad:

```bash
# Ejecutar solo pruebas de baja prioridad
pytest -m low

# Ejecutar solo pruebas de media prioridad (debes declarar @pytest.mark.medium)
pytest -m medium

```

### Ejecutar una prueba específica:

```bash
pytest features/steps/test_register.py

```

----------

## 📊 Reportes con Allure

1.  🔧 Instala Allure CLI:
    
    -   **Windows:** `scoop install allure` o desde [GitHub](https://github.com/allure-framework/allure2/releases)
        
    -   **macOS:** `brew install allure`
        
    -   **Linux:** Ver [documentación oficial](https://docs.qameta.io/allure/)
        
2.  🧾 Ejecuta pruebas y visualiza reportes:
    

```bash
pytest --alluredir=allure

# Para ver el reporte:
allure serve allure

```

----------

## 🔌 Personalización y Extensión

### ➕ Añadir nuevos escenarios

1.  Crea o edita archivos `.feature`:
    

```gherkin
Feature: Nueva funcionalidad

@medium
Scenario: Nuevo escenario de prueba
    Given alguna condición inicial
    When ocurre alguna acción
    Then se obtiene un resultado esperado

```

2.  Implementa los pasos en un archivo Python:
    

```python
from pytest_bdd import given, then, when, scenario
import allure

@scenario("nueva_funcionalidad.feature", "Nuevo escenario de prueba")
@allure.suite("Nueva Suite")
def test_nueva_funcionalidad():
    pass

@given('alguna condición inicial')
def step_condicion_inicial(driver):
    # Implementación aquí
    pass

```

### 🧱 Crear nuevos Page Objects

1.  Agrega un nuevo archivo con localizadores en `pages/pages_objects/`:
    

```python
from selenium.webdriver.common.by import By

class NuevaPagina:
    elemento1 = (By.ID, "id_elemento1")
    elemento2 = (By.XPATH, "//ruta/al/elemento2")

```

2.  Crea su clase de acciones correspondiente en `pages/actions/`:
    

```python
from .base_actions import BaseActions
from pages.pages_objects.nueva_pagina import NuevaPagina

class NuevaPaginaActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
    
    def nueva_accion(self):
        self.element_click(NuevaPagina.elemento1)

```

----------

## 🧩 Consejos Útiles

-   🔁 Usa fixtures para reutilizar lógica de setup.
    
-   🗂️ Agrupa tus tests por módulos funcionales.
    
-   📌 Usa `@pytest.mark.skip` o `@pytest.mark.xfail` para pruebas condicionales.
    
-   🚦 Configura GitHub Actions o Jenkins para CI/CD.
    

----------

## 📌Notas importantes

- Esto es un proyecto que he seguido de un curso de Selenium [Youtube](https://www.youtube.com/@TesterTestarudo)
- Enlace al curso de Selenium [Curso](https://youtube.com/playlist?list=PLc-q67wAZF0N6N9YeCtK6BP_RS4d1v-3_&si=iOdCvZbwmEQ1k6xg)
