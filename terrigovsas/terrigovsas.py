import reflex as rx
from typing import List

# Configuración de colores basada en el logo
colors = {
    "primary": "#007BFF",
    "secondary": "#00CFFF", 
    "accent": "#00D29E",
    "dark": "#0C1220",
    "light": "#FFFFFF",
    "gray": "#6C757D"
}

# Configuración de la aplicación
config = rx.Config(
    app_name="terrigo_landing",
    tailwind={
        "theme": {
            "extend": {
                "colors": colors,
                "fontFamily": {
                    "sans": ["Inter", "system-ui", "sans-serif"]
                }
            }
        }
    }
)

def navbar() -> rx.Component:
    """Componente de navegación principal"""
    return rx.box(
        rx.hstack(
            # Logo y nombre de la empresa
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    alt="Terrigo Logo",
                    width="50px",
                    height="50px"
                ),
                rx.vstack(
                    rx.text(
                        "Terrigo S.A.S.",
                        size="6",
                        weight="bold",
                        color=colors["dark"]
                    ),
                    rx.text(
                        "Innovación y Desarrollo para el Territorio",
                        size="2",
                        color=colors["gray"],
                        font_style="italic"
                    ),
                    spacing="1",
                    align="start"
                ),
                spacing="4",
                align="center"
            ),
            
            # Menú de navegación
            rx.hstack(
                rx.link("Inicio", href="#inicio", color=colors["dark"], _hover={"color": colors["primary"]}),
                rx.link("Servicios", href="#servicios", color=colors["dark"], _hover={"color": colors["primary"]}),
                rx.link("Sobre Nosotros", href="#sobre-nosotros", color=colors["dark"], _hover={"color": colors["primary"]}),
                rx.link("Contacto", href="#contacto", color=colors["dark"], _hover={"color": colors["primary"]}),
                spacing="6",
                display=["none", "none", "flex"]
            ),
            
            justify="between",
            align="center",
            width="100%"
        ),
        background=colors["light"],
        padding="1rem 2rem",
        box_shadow="0 2px 4px rgba(0,0,0,0.1)",
        position="sticky",
        top="0",
        z_index="1000"
    )

def hero_section() -> rx.Component:
    """Sección hero principal"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Transformamos Territorios con Tecnología",
                    size="9",
                    color=colors["light"],
                    text_align="center",
                    font_weight="bold",
                    line_height="1.2"
                ),
                rx.text(
                    "Soluciones inteligentes para la gestión pública",
                    size="5",
                    color=colors["light"],
                    text_align="center",
                    opacity="0.9"
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("message-circle", size=20),
                            rx.text("Habla con nosotros por WhatsApp", size="4", weight="medium"),
                            spacing="2",
                            align="center"
                        ),
                        size="4",
                        padding="1rem 2rem",
                        background=colors["accent"],
                        color=colors["light"],
                        border="none",
                        border_radius="50px",
                        _hover={
                            "background": "#00B889",
                            "transform": "translateY(-2px)",
                            "box_shadow": "0 8px 25px rgba(0,210,158,0.3)"
                        },
                        transition="all 0.3s ease"
                    ),
                    href="https://wa.me/573001234567",
                    is_external=True
                ),
                spacing="6",
                align="center",
                padding="4rem 2rem"
            ),
            max_width="1200px"
        ),
        id="inicio",
        background=f"linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%)",
        min_height="100vh",
        display="flex",
        align_items="center",
        position="relative",
        _before={
            "content": "''",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "right": "0",
            "bottom": "0",
            "background": "url('/hero-bg.jpg') center/cover",
            "opacity": "0.1",
            "z_index": "-1"
        }
    )

def service_card(title: str, description: str, icon: str) -> rx.Component:
    """Componente de tarjeta de servicio"""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=40, color=colors["primary"]),
                padding="1rem",
                background=f"linear-gradient(135deg, {colors['primary']}15, {colors['secondary']}15)",
                border_radius="50%",
                margin_bottom="1rem"
            ),
            rx.heading(title, size="5", color=colors["dark"], text_align="center"),
            rx.text(
                description,
                size="3",
                color=colors["gray"],
                text_align="center",
                line_height="1.5"
            ),
            spacing="3",
            align="center"
        ),
        padding="2rem",
        background=colors["light"],
        border_radius="12px",
        box_shadow="0 4px 20px rgba(0,0,0,0.1)",
        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": "0 8px 30px rgba(0,123,255,0.2)"
        },
        transition="all 0.3s ease",
        height="100%"
    )

def services_section() -> rx.Component:
    """Sección de servicios"""
    services = [
        {
            "title": "Observatorios de Datos",
            "description": "Plataformas avanzadas para la visualización y análisis de datos territoriales en tiempo real.",
            "icon": "bar-chart-3"
        },
        {
            "title": "Decisiones Basadas en Datos",
            "description": "Herramientas de inteligencia artificial para optimizar la toma de decisiones públicas.",
            "icon": "brain"
        },
        {
            "title": "Automatización de Contratación",
            "description": "Sistemas inteligentes para agilizar y transparentar los procesos de contratación estatal.",
            "icon": "file-text"
        },
        {
            "title": "Transformación Digital",
            "description": "Modernización integral de procesos y servicios en entidades públicas.",
            "icon": "smartphone"
        },
        {
            "title": "Inteligencia Artificial",
            "description": "Soluciones de IA aplicadas a la gestión pública y análisis predictivo.",
            "icon": "cpu"
        },
        {
            "title": "Integración de Plataformas",
            "description": "Conectamos CiviData, UnityGov y TerriGov para un ecosistema digital completo.",
            "icon": "network"
        }
    ]
    
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Nuestros Servicios",
                    size="8",
                    color=colors["dark"],
                    text_align="center",
                    margin_bottom="1rem"
                ),
                rx.text(
                    "Ofrecemos soluciones tecnológicas integrales para la modernización del sector público",
                    size="4",
                    color=colors["gray"],
                    text_align="center",
                    margin_bottom="3rem"
                ),
                rx.grid(
                    *[service_card(service["title"], service["description"], service["icon"]) 
                      for service in services],
                    columns="3",
                    spacing="6",
                    width="100%"
                ),
                spacing="6",
                align="center"
            ),
            max_width="1200px",
            padding="4rem 2rem"
        ),
        id="servicios",
        background="#F8F9FA"
    )

def about_section() -> rx.Component:
    """Sección sobre nosotros"""
    return rx.box(
        rx.container(
            rx.grid(
                # Columna izquierda - Contenido
                rx.vstack(
                    rx.heading(
                        "Sobre Nosotros",
                        size="8",
                        color=colors["dark"],
                        margin_bottom="2rem"
                    ),
                    rx.text(
                        "Terrigo S.A.S. es una empresa líder en transformación digital para el sector público, "
                        "formando parte de la alianza estratégica con UnityGov y CiviData. Nos especializamos "
                        "en crear soluciones tecnológicas innovadoras que optimizan la gestión territorial.",
                        size="4",
                        color=colors["gray"],
                        line_height="1.6",
                        margin_bottom="2rem"
                    ),
                    
                    # Valores
                    rx.vstack(
                        rx.heading("Nuestra Visión", size="5", color=colors["primary"]),
                        rx.text(
                            "Ser el aliado tecnológico de los territorios, impulsando la innovación "
                            "y la eficiencia en la gestión pública a través de soluciones digitales.",
                            size="3",
                            color=colors["gray"],
                            line_height="1.5"
                        ),
                        spacing="2",
                        align="start",
                        margin_bottom="2rem"
                    ),
                    
                    rx.hstack(
                        rx.vstack(
                            rx.box(
                                rx.icon("lightbulb", size=24, color=colors["accent"]),
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Innovación", size="3", weight="bold", color=colors["dark"]),
                            align="center",
                            spacing="2"
                        ),
                        rx.vstack(
                            rx.box(
                                rx.icon("eye", size=24, color=colors["accent"]),
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Transparencia", size="3", weight="bold", color=colors["dark"]),
                            align="center",
                            spacing="2"
                        ),
                        rx.vstack(
                            rx.box(
                                rx.icon("zap", size=24, color=colors["accent"]),
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Eficiencia", size="3", weight="bold", color=colors["dark"]),
                            align="center",
                            spacing="2"
                        ),
                        spacing="4",
                        justify="start"
                    ),
                    
                    align="start",
                    spacing="4"
                ),
                
                # Columna derecha - Imagen destacada
                rx.box(
                    rx.box(
                        rx.vstack(
                            rx.icon("map", size=60, color=colors["primary"]),
                            rx.text("Territorio Digital", size="5", weight="bold", color=colors["dark"]),
                            rx.text("Visualización de datos territoriales", size="3", color=colors["gray"]),
                            spacing="3",
                            align="center"
                        ),
                        padding="3rem",
                        background=f"linear-gradient(135deg, {colors['primary']}10, {colors['secondary']}10)",
                        border_radius="16px",
                        border=f"2px solid {colors['primary']}30",
                        text_align="center",
                        height="100%",
                        display="flex",
                        align_items="center",
                        justify_content="center"
                    ),
                    height="400px"
                ),
                
                columns="2",
                spacing="6",
                align="center"
            ),
            max_width="1200px",
            padding="4rem 2rem"
        ),
        id="sobre-nosotros",
        background=colors["light"]
    )

def contact_section() -> rx.Component:
    """Sección de contacto"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Contacto",
                    size="8",
                    color=colors["light"],
                    text_align="center",
                    margin_bottom="2rem"
                ),
                rx.text(
                    "¿Listo para transformar tu territorio? Contáctanos y descubre cómo podemos ayudarte",
                    size="4",
                    color=colors["light"],
                    text_align="center",
                    opacity="0.9",
                    margin_bottom="3rem"
                ),
                
                rx.grid(
                    rx.vstack(
                        rx.icon("mail", size=30, color=colors["accent"]),
                        rx.text("Email", size="4", weight="bold", color=colors["light"]),
                        rx.text("contacto@terrigo.com", size="3", color=colors["light"], opacity="0.8"),
                        spacing="2",
                        align="center"
                    ),
                    rx.vstack(
                        rx.icon("message-circle", size=30, color=colors["accent"]),
                        rx.text("WhatsApp", size="4", weight="bold", color=colors["light"]),
                        rx.text("+57 300 123 4567", size="3", color=colors["light"], opacity="0.8"),
                        spacing="2",
                        align="center"
                    ),
                    rx.vstack(
                        rx.icon("map-pin", size=30, color=colors["accent"]),
                        rx.text("Ubicación", size="4", weight="bold", color=colors["light"]),
                        rx.text("Colombia", size="3", color=colors["light"], opacity="0.8"),
                        spacing="2",
                        align="center"
                    ),
                    columns="3",
                    spacing="6",
                    margin_bottom="3rem"
                ),
                
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("message-circle", size=24),
                            rx.text("Iniciar Conversación", size="4", weight="medium"),
                            spacing="2",
                            align="center"
                        ),
                        size="4",
                        padding="1rem 2rem",
                        background=colors["accent"],
                        color=colors["light"],
                        border="none",
                        border_radius="50px",
                        _hover={
                            "background": "#00B889",
                            "transform": "translateY(-2px)",
                            "box_shadow": "0 8px 25px rgba(0,210,158,0.3)"
                        },
                        transition="all 0.3s ease"
                    ),
                    href="https://wa.me/573001234567",
                    is_external=True
                ),
                
                spacing="6",
                align="center"
            ),
            max_width="1200px",
            padding="4rem 2rem"
        ),
        id="contacto",
        background=f"linear-gradient(135deg, {colors['dark']} 0%, {colors['primary']} 100%)"
    )

def footer() -> rx.Component:
    """Pie de página"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "© 2024 Terrigo S.A.S. - Innovación y Desarrollo para el Territorio",
                        size="3",
                        color=colors["gray"]
                    ),
                    rx.hstack(
                        rx.link(
                            rx.icon("linkedin", size=20, color=colors["gray"]),
                            href="#",
                            _hover={"color": colors["primary"]}
                        ),
                        rx.link(
                            rx.icon("github", size=20, color=colors["gray"]),
                            href="#",
                            _hover={"color": colors["primary"]}
                        ),
                        spacing="3"
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    flex_wrap="wrap"
                ),
                spacing="4",
                align="center"
            ),
            max_width="1200px",
            padding="2rem"
        ),
        background="#F8F9FA",
        border_top=f"1px solid {colors['gray']}30"
    )

def index() -> rx.Component:
    """Página principal"""
    return rx.box(
        navbar(),
        hero_section(),
        services_section(),
        about_section(),
        contact_section(),
        footer(),
        font_family="Inter, system-ui, sans-serif"
    )

# Configuración de la aplicación
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        accent_color="blue"
    )
)

app.add_page(index, route="/")