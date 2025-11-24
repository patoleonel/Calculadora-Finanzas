# Calculadora de Metas Financieras

Una aplicación web construida con Flask que ayuda a los usuarios a planificar sus objetivos financieros. Permite calcular cuánto ahorrar mensualmente para llegar a una meta en una fecha específica, o estimar cuándo se alcanzará una meta dada una contribución mensual fija.

## Características

-   **Meta basada en Tiempo**: Calcula la contribución mensual necesaria para alcanzar un monto objetivo en una fecha determinada.
-   **Meta basada en Contribución**: Estima la fecha en la que se alcanzará el objetivo dado un ahorro mensual fijo.
-   **Cálculo de Interés Compuesto**: Considera una tasa de interés anual para proyecciones más realistas.
-   **Interfaz Intuitiva**: Diseño limpio y fácil de usar.

## Tecnologías

-   Python 3.x
-   Flask
-   HTML5 / CSS3

## Instalación Local

Sigue estos pasos para ejecutar la aplicación en tu computadora:

1.  **Clonar el repositorio**
    ```bash
    git clone <tu-repo-url>
    cd Calculadora-Finanzas
    ```

2.  **Crear un entorno virtual**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la aplicación**
    ```bash
    python app.py
    ```

5.  **Abrir en el navegador**
    Ve a [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Despliegue

Esta aplicación está configurada para ser desplegada fácilmente en **Vercel**.

-   El archivo `vercel.json` contiene la configuración necesaria.
-   El archivo `requirements.txt` lista las dependencias necesarias.

## Estructura del Proyecto

-   `app.py`: Contiene la lógica del servidor Flask y los cálculos financieros.
-   `templates/`: Contiene los archivos HTML (Jinja2).
-   `static/`: Contiene los archivos CSS y recursos estáticos.
