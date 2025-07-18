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
    app_name="terrigov_landing",
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
    """Componente de navegación principal - Ahora responsive"""
    return rx.box(
        rx.hstack(
            # Logo y nombre de la empresa
            rx.hstack(
                rx.image(
                    src="https://i.postimg.cc/PJgFKg6x/Icon-2-SVG.png",
                    alt="Logo de la empresa",
                    width=["40px", "45px", "50px"]  # Responsive: móvil, tablet, desktop
                ),
                rx.vstack(
                    rx.text(
                        "TerriGov S.A.S.",
                        size=["4", "5", "6"],  # Responsive text size
                        weight="bold",
                        color=colors["dark"]
                    ),
                    rx.text(
                        "Innovación y Desarrollo para el Territorio",
                        size=["1", "2", "2"],  # Responsive text size
                        color=colors["gray"],
                        font_style="italic",
                        display=["none", "block", "block"]  # Oculto en móvil
                    ),
                    spacing="1",
                    align="start"
                ),
                spacing=["2", "3", "4"],  # Responsive spacing
                align="center"
            ),
            
            # Menú de navegación - Responsive
            rx.hstack(
                rx.link("Inicio", href="#inicio", color=colors["dark"], _hover={"color": colors["primary"]}, size=["2", "3", "3"]),
                rx.link("Servicios", href="#servicios", color=colors["dark"], _hover={"color": colors["primary"]}, size=["2", "3", "3"]),
                rx.link("Sobre Nosotros", href="#sobre-nosotros", color=colors["dark"], _hover={"color": colors["primary"]}, size=["2", "3", "3"]),
                rx.link("Contacto", href="#contacto", color=colors["dark"], _hover={"color": colors["primary"]}, size=["2", "3", "3"]),
                spacing=["2", "4", "6"],  # Responsive spacing
                display=["none", "none", "flex"]  # Oculto en móvil y tablet pequeño
            ),
            
            # Menú hamburguesa para móvil (placeholder)
            rx.box(
                rx.icon("menu", size=24, color=colors["dark"]),
                display=["block", "block", "none"],  # Visible solo en móvil/tablet
                cursor="pointer"
            ),
            
            justify="between",
            align="center",
            width="100%"
        ),
        background=colors["light"],
        padding=["0.5rem 1rem", "0.75rem 1.5rem", "1rem 2rem"],  # Responsive padding
        box_shadow="0 2px 4px rgba(0,0,0,0.1)",
        position="sticky",
        top="0",
        z_index="1000"
    )

def hero_section() -> rx.Component:
    """Sección hero principal - Responsive"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Transformamos Territorios con Tecnología",
                    size=["6", "8", "9"],  # Responsive heading size
                    color=colors["light"],
                    text_align="center",
                    font_weight="bold",
                    line_height="1.2"
                ),
                rx.text(
                    "Soluciones inteligentes para la gestión pública",
                    size=["3", "4", "5"],  # Responsive text size
                    color=colors["light"],
                    text_align="center",
                    opacity="0.9"
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("message-circle", size=[16, 18, 20]),  # Responsive icon size
                            rx.text("Habla con nosotros por WhatsApp", size=["3", "3", "4"], weight="medium"),
                            spacing="2",
                            align="center"
                        ),
                        size=["3", "3", "4"],  # Responsive button size
                        padding=["0.75rem 1.5rem", "0.875rem 1.75rem", "1rem 2rem"],  # Responsive padding
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
                    href="https://wa.me/573207803362",
                    is_external=True
                ),
                spacing=["4", "5", "6"],  # Responsive spacing
                align="center",
                padding=["2rem 1rem", "3rem 1.5rem", "4rem 2rem"]  # Responsive padding
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
    """Componente de tarjeta de servicio - Responsive"""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=[28, 35, 40], color=colors["primary"]),  # Responsive icon size
                padding=["0.75rem", "0.875rem", "1rem"],  # Responsive padding
                background=f"linear-gradient(135deg, {colors['primary']}15, {colors['secondary']}15)",
                border_radius="50%",
                margin_bottom=["0.75rem", "0.875rem", "1rem"]  # Responsive margin
            ),
            rx.heading(title, size=["4", "4", "5"], color=colors["dark"], text_align="center"),  # Responsive heading
            rx.text(
                description,
                size=["2", "3", "3"],  # Responsive text size
                color=colors["gray"],
                text_align="center",
                line_height="1.5"
            ),
            spacing=["2", "2", "3"],  # Responsive spacing
            align="center"
        ),
        padding=["1.5rem", "1.75rem", "2rem"],  # Responsive padding
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
    """Sección de servicios - Responsive"""
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
            "title": "Equipamiento Tecnológico",
            "description": "Computadores, servidores, redes y toda la tecnología necesaria para tu transformación digital.",
            "icon": "network"
        }
    ]
    
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Nuestros Servicios",
                    size=["6", "7", "8"],  # Responsive heading
                    color=colors["dark"],
                    text_align="center",
                    margin_bottom="1rem"
                ),
                rx.text(
                    "Ofrecemos soluciones tecnológicas integrales para la modernización del sector público",
                    size=["3", "3", "4"],  # Responsive text
                    color=colors["gray"],
                    text_align="center",
                    margin_bottom="3rem"
                ),
                rx.grid(
                    *[service_card(service["title"], service["description"], service["icon"]) 
                      for service in services],
                    columns=["1", "2", "3"],  # Responsive grid: 1 columna en móvil, 2 en tablet, 3 en desktop
                    spacing=["4", "5", "6"],  # Responsive spacing
                    width="100%"
                ),
                spacing=["4", "5", "6"],  # Responsive spacing
                align="center"
            ),
            max_width="1200px",
            padding=["2rem 1rem", "3rem 1.5rem", "4rem 2rem"]  # Responsive padding
        ),
        id="servicios",
        background="#F8F9FA"
    )

def about_section() -> rx.Component:
    """Sección sobre nosotros - Responsive"""
    return rx.box(
        rx.container(
            rx.grid(
                # Columna izquierda - Contenido
                rx.vstack(
                    rx.heading(
                        "Sobre Nosotros",
                        size=["6", "7", "8"],  # Responsive heading
                        color=colors["dark"],
                        margin_bottom="2rem"
                    ),
                    rx.text(
                        "TerriGov S.A.S. es una empresa líder en transformación digital para el sector público, "
                        "formando parte de la alianza estratégica con el Territorio. Nos especializamos "
                        "en crear soluciones tecnológicas innovadoras que optimizan la gestión territorial.",
                        size=["3", "3", "4"],  # Responsive text
                        color=colors["gray"],
                        line_height="1.6",
                        margin_bottom="2rem"
                    ),
                    
                    # Valores
                    rx.vstack(
                        rx.heading("Nuestra Visión", size=["4", "4", "5"], color=colors["primary"]),  # Responsive heading
                        rx.text(
                            "Ser el aliado tecnológico de los territorios, impulsando la innovación "
                            "y la eficiencia en la gestión pública a través de soluciones digitales.",
                            size=["2", "3", "3"],  # Responsive text
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
                                rx.icon("lightbulb", size=[18, 20, 24], color=colors["accent"]),  # Responsive icon
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Innovación", size=["2", "2", "3"], weight="bold", color=colors["dark"]),  # Responsive text
                            align="center",
                            spacing="2"
                        ),
                        rx.vstack(
                            rx.box(
                                rx.icon("eye", size=[18, 20, 24], color=colors["accent"]),  # Responsive icon
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Transparencia", size=["2", "2", "3"], weight="bold", color=colors["dark"]),  # Responsive text
                            align="center",
                            spacing="2"
                        ),
                        rx.vstack(
                            rx.box(
                                rx.icon("zap", size=[18, 20, 24], color=colors["accent"]),  # Responsive icon
                                padding="0.5rem",
                                background=f"{colors['accent']}20",
                                border_radius="8px"
                            ),
                            rx.text("Eficiencia", size=["2", "2", "3"], weight="bold", color=colors["dark"]),  # Responsive text
                            align="center",
                            spacing="2"
                        ),
                        spacing=["2", "3", "4"],  # Responsive spacing
                        justify="start",
                        flex_wrap="wrap"  # Permite que se envuelvan en móvil
                    ),
                    
                    align="start",
                    spacing="4"
                ),
                
                # Columna derecha - Imagen destacada
                rx.box(
                    rx.box(
                        rx.image(
                            src="https://i.postimg.cc/5yWfQRwB/Imagen-Terrigov.png",
                            alt="TerriGov - Territorio Digital",
                            width=["300px", "400px", "450px"],  # Responsive image size
                            height=["300px", "400px", "450px"],  # Responsive image size
                            object_fit="contain",
                            border_radius="8px"
                        ),
                        padding=["2rem", "2.5rem", "3rem"],  # Responsive padding
                        background=f"linear-gradient(135deg, {colors['primary']}10, {colors['secondary']}10)",
                        border_radius="16px",
                        border=f"2px solid {colors['primary']}30",
                        text_align="center",
                        height="100%",
                        display="flex",
                        align_items="center",
                        justify_content="center"
                    ),
                    height=["300px", "400px", "400px"]  # Responsive height
                ),
                
                columns=["1", "1", "2"],  # Responsive grid: 1 columna en móvil/tablet, 2 en desktop
                spacing=["4", "5", "6"],  # Responsive spacing
                align="center"
            ),
            max_width="1200px",
            padding=["2rem 1rem", "3rem 1.5rem", "4rem 2rem"]  # Responsive padding
        ),
        id="sobre-nosotros",
        background=colors["light"]
    )

def contact_section() -> rx.Component:
    """Sección de contacto - Responsive"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Contacto",
                    size=["6", "7", "8"],  # Responsive heading
                    color=colors["light"],
                    text_align="center",
                    margin_bottom="2rem"
                ),
                rx.text(
                    "¿Listo para transformar tu territorio? Contáctanos y descubre cómo podemos ayudarte",
                    size=["3", "3", "4"],  # Responsive text
                    color=colors["light"],
                    text_align="center",
                    opacity="0.9",
                    margin_bottom="3rem"
                ),
                
                rx.grid(
                    rx.vstack(
                        rx.icon("mail", size=[24, 27, 30], color=colors["accent"]),  # Responsive icon
                        rx.text("Email", size=["3", "3", "4"], weight="bold", color=colors["light"]),  # Responsive text
                        rx.text("info@terrigov.co", size=["2", "2", "3"], color=colors["light"], opacity="0.8"),  # Responsive text
                        spacing="2",
                        align="center"
                    ),
                    rx.vstack(
                        rx.icon("message-circle", size=[24, 27, 30], color=colors["accent"]),  # Responsive icon
                        rx.text("WhatsApp", size=["3", "3", "4"], weight="bold", color=colors["light"]),  # Responsive text
                        rx.text("+57 320 780 3362", size=["2", "2", "3"], color=colors["light"], opacity="0.8"),  # Responsive text
                        spacing="2",
                        align="center"
                    ),
                    rx.vstack(
                        rx.icon("map-pin", size=[24, 27, 30], color=colors["accent"]),  # Responsive icon
                        rx.text("Ubicación", size=["3", "3", "4"], weight="bold", color=colors["light"]),  # Responsive text
                        rx.text("Colombia", size=["2", "2", "3"], color=colors["light"], opacity="0.8"),  # Responsive text
                        spacing="2",
                        align="center"
                    ),
                    columns=["1", "3", "3"],  # Responsive grid: 1 columna en móvil, 3 en tablet/desktop
                    spacing=["4", "5", "6"],  # Responsive spacing
                    margin_bottom="3rem"
                ),
                
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("message-circle", size=[18, 20, 24]),  # Responsive icon
                            rx.text("Iniciar Conversación", size=["3", "3", "4"], weight="medium"),  # Responsive text
                            spacing="2",
                            align="center"
                        ),
                        size=["3", "3", "4"],  # Responsive button size
                        padding=["0.75rem 1.5rem", "0.875rem 1.75rem", "1rem 2rem"],  # Responsive padding
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
                    href="https://wa.me/573207803362",
                    is_external=True
                ),
                
                spacing=["4", "5", "6"],  # Responsive spacing
                align="center"
            ),
            max_width="1200px",
            padding=["2rem 1rem", "3rem 1.5rem", "4rem 2rem"]  # Responsive padding
        ),
        id="contacto",
        background=f"linear-gradient(135deg, {colors['dark']} 0%, {colors['primary']} 100%)"
    )

def footer() -> rx.Component:
    """Pie de página - Responsive"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "© 2023 TerriGov S.A.S. - Innovación y Desarrollo para el Territorio",
                        size=["2", "2", "3"],  # Responsive text
                        color=colors["gray"],
                        text_align=["center", "center", "left"]  # Centrado en móvil
                    ),
                    rx.hstack(
                        rx.link(
                            rx.icon("linkedin", size=[16, 18, 20], color=colors["gray"]),  # Responsive icon
                            href="#",
                            _hover={"color": colors["primary"]}
                        ),
                        rx.link(
                            rx.icon("instagram", size=[16, 18, 20], color=colors["gray"]),  # Responsive icon
                            href="#",
                            _hover={"color": colors["primary"]}
                        ),
                        spacing="3"
                    ),
                    justify=["center", "center", "between"],  # Centrado en móvil, entre en desktop
                    align="center",
                    width="100%",
                    flex_wrap="wrap",
                    direction=["column", "column", "row"],  # Columna en móvil, fila en desktop
                    spacing=["2", "2", "0"]  # Espaciado en móvil
                ),
                spacing="4",
                align="center"
            ),
            max_width="1200px",
            padding=["1rem", "1.5rem", "2rem"]  # Responsive padding
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