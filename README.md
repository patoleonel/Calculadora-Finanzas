# Financial Goals App

Una aplicación web simple para rastrear tus objetivos financieros, construida con Flask.

## Características

- Crear objetivos basados en tiempo (fecha objetivo) o contribución mensual.
- Visualizar el progreso con barras de progreso.
- Cálculo automático de contribuciones mensuales o fechas estimadas.

## Instalación Local

1.  Clonar el repositorio:
    ```bash
    git clone <tu-repo-url>
    cd financial_goals_app
    ```

2.  Crear un entorno virtual e instalar dependencias:
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  Ejecutar la aplicación:
    ```bash
    python app.py
    ```

4.  Abrir en el navegador: `http://127.0.0.1:5000`

## Despliegue

Esta aplicación está lista para ser desplegada en plataformas como Render, Railway o Heroku.

### Render / Railway

1.  Conecta tu repositorio de GitHub.
2.  El servicio detectará automáticamente el archivo `Procfile` y `requirements.txt`.
3.  **Configuración de Variables de Entorno**:
    - `SECRET_KEY`: Una cadena aleatoria segura.
    - `DATABASE_URL`: La URL de tu base de datos PostgreSQL (proporcionada por el servicio de hosting).

## Estructura del Proyecto

- `app.py`: Aplicación principal Flask.
- `models.py`: Modelos de base de datos SQLAlchemy.
- `templates/`: Plantillas HTML.
- `static/`: Archivos estáticos (CSS).
