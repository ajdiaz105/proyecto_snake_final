
# Snake Retro 2D (Python + turtle)

Versión clásica **monocromática (blanco/negro)** del juego Snake.
Sin menús ni pantallas extra: ejecutas y juegas. Hecho con la librería estándar `turtle` (no requiere instalar paquetes).

## Características
- Fondo negro, sprites cuadrados blancos (estética retro en "bits").
- Movimiento en **grid** (STEP=20 px).
- Comida cuadrada (mismo estilo que la serpiente).
- Marcador de **SCORE** en la parte superior.
- **Pausa (P)**, **Reiniciar (R)** y **Salir (Esc)**.
- Reinicio automático al chocar con borde o cuerpo.
- Opción de **velocidad progresiva** por puntaje (activable desde `game.py`).

## Controles
- Flechas: mover la serpiente (sin reversa inmediata).
- P: Pausa/Continuar.
- R: Reiniciar cuando pierdes (o en cualquier momento).
- Esc: Salir.

## Estructura
```
snake_retro_2d/
└─ src/
   ├─ main.py
   ├─ game.py
   ├─ snake.py
   ├─ food.py
   └─ score.py
```

## Requisitos
- Python 3.8+
- No requiere instalar dependencias (usa `turtle`, estándar en CPython).

## Ejecución
```bash
python src/main.py
```

> Si estás en Windows y no abre la ventana, ejecuta como `python.exe` (no `py`) o verifica tu instalación de Python.

## Configuración rápida
- Ajusta tamaño de ventana y grid en `game.py`:
  - `WIDTH`, `HEIGHT`, `STEP`, `DELAY_BASE`, `SPEEDUP_EVERY`, `DELAY_MIN`.
- Cambia estética (sigue siendo monocromo) en `snake.py`/`food.py` (`shape`, `color`).

¡Disfruta!
