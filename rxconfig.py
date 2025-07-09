import reflex as rx
import os

config = rx.Config(
    app_name="terrigovsas",
    plugins=[rx.plugins.TailwindV3Plugin()],
    backend_host="0.0.0.0",
    backend_port=3000,
    frontend_port=3000,
    # Intenta agregar esto 
    show_reflex_badge=False,
)