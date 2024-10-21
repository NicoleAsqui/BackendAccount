# Proyecto de Gestión de Cuentas Bancarias

Este proyecto es una aplicación de gestión de cuentas bancarias, que permite crear cuentas con nombre, tipo de cuenta y saldo. Está estructurada siguiendo la arquitectura hexagonal, lo que facilita la separación de responsabilidades y la mantenibilidad del código. 

## Estructura del Proyecto

El proyecto se organiza en varias capas:

- **Capa de Controladores**: Maneja las solicitudes y respuestas de la API.
- **Capa de Casos de Uso**: Contiene la lógica de negocio de la aplicación.
- **Capa de Repositorios**: Se encarga del acceso a los datos y la persistencia de las cuentas.

## Instalación y Configuración del Entorno

Para crear el entorno de desarrollo y ejecutar la aplicación, sigue estos pasos:

1. **Clona el repositorio**:

   ```
   git clone https://github.com/NicoleAsqui/BackendAccount
    ```

2. **Ejecuta el programa**:

En Windows:

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

En macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


Crea un archivo .env:

En la raíz del proyecto, crea un archivo llamado .env y agrega la URL de tu ambiente, o usa el .env.example. Por ejemplo:

    URL=<LOCALHOST>

Corre el back con:

    uvicorn app.api.main:app --reload

    
3. **Ejecuta las pruebas**:

Las pruebas están escritas utilizando pytest y fixtures para garantizar una buena cobertura y calidad del código. Para ejecutar todas las pruebas, utiliza:

    pytest tests


Para mantener la calidad del código, se ha configurado flake8 como linter. Para ejecutar el linter, utiliza:

    flake8 --config=.flake8

Si usas pre-commit, puedes ejecutar todos los ganchos configurados con:

    pre-commit run --all-files
