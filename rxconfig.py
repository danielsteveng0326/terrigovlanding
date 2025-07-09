import reflex as rx
import os

config = rx.Config(
    app_name="terrigovsas",  # Cambia este nombre por el de tu app
    plugins=[rx.plugins.TailwindV3Plugin()],
    backend_host="0.0.0.0",
    backend_port=3000,
    frontend_port=3000,
)