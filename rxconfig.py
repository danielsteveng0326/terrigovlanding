import reflex as rx
import os

config = rx.Config(
    app_name="terrigovsas",
    # Para production en Railway
    api_url=os.getenv("RAILWAY_PUBLIC_DOMAIN", "http://localhost:8000"),
    deploy_url=os.getenv("RAILWAY_PUBLIC_DOMAIN", "http://localhost:3000"),
    # Configuración de puertos
    frontend_port=3000,
    backend_port=3000,
    # Configuración de producción
    env=rx.Env.PROD if os.getenv("RAILWAY_ENVIRONMENT") else rx.Env.DEV,
)