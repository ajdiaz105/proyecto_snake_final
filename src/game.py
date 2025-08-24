
import turtle as t
import time
from snake import Snake
from food import Food
from score import Score
import random

# ---------------- Configuración global (retro) ----------------
WIDTH, HEIGHT = 600, 600
STEP = 20

# Velocidad base y progresión (ajusta si quieres)
DELAY_BASE = 0.10      # más pequeño = más rápido
SPEEDUP_EVERY = 5      # cada N comidas reduce delay
DELAY_DECREASE = 0.005
DELAY_MIN = 0.03

# Estados de juego
INIT, RUNNING, PAUSED, GAME_OVER = "INIT", "RUNNING", "PAUSED", "GAME_OVER"

class Game:
    def __init__(self):
        # Ventana
        self.wn = t.Screen()
        self.wn.title("Snake Retro 2D")
        self.wn.bgcolor("black")
        self.wn.setup(width=WIDTH, height=HEIGHT)
        self.wn.tracer(0)

        # Entidades
        self.snake = Snake(step=STEP)
        self.food = Food(WIDTH, HEIGHT, STEP)
        self.score = Score(WIDTH, HEIGHT)

        # Estado
        self.state = INIT
        self.delay = DELAY_BASE
        self._register_keys()

        # Inicialización
        self.reset(full=True)

    # ---------------- Input ----------------
    def _register_keys(self):
        self.wn.listen()
        self.wn.onkeypress(lambda: self._dir(0,  STEP), "Up")
        self.wn.onkeypress(lambda: self._dir(0, -STEP), "Down")
        self.wn.onkeypress(lambda: self._dir(-STEP, 0), "Left")
        self.wn.onkeypress(lambda: self._dir( STEP, 0), "Right")
        self.wn.onkeypress(self.toggle_pause, "p")
        self.wn.onkeypress(self.toggle_pause, "P")
        self.wn.onkeypress(self.reset, "r")
        self.wn.onkeypress(self.reset, "R")
        self.wn.onkeypress(self.exit_game, "Escape")

    def _dir(self, dx, dy):
        if self.state != RUNNING:
            return
        self.snake.set_direction(dx, dy)

    def toggle_pause(self):
        if self.state == RUNNING:
            self.state = PAUSED
            self._overlay_text("PAUSA - Presiona P para continuar")
        elif self.state == PAUSED:
            self.state = RUNNING

    def exit_game(self):
        try:
            t.bye()
        except Exception:
            pass

    # ---------------- Ciclo de vida ----------------
    def reset(self, full=False):
        # Reinicia serpiente, comida y score
        self.snake.reset()
        self.food.place_away_from(self.snake.occupied_positions())
        self.score.reset()
        self.delay = DELAY_BASE
        self.state = RUNNING

    def _overlay_text(self, text):
        # Texto centrado temporal (usa el mismo pen de score para no crear nuevos turtle)
        self.score.pen2.clear()
        self.score.pen2.goto(0, 0)
        self.score.pen2.write(text, align="center", font=("Courier", 16, "normal"))

    def _clear_overlay(self):
        self.score.pen2.clear()

    def _speedup_if_needed(self):
        if self.score.value > 0 and self.score.value % SPEEDUP_EVERY == 0:
            self.delay = max(DELAY_MIN, self.delay - DELAY_DECREASE)

    def run(self):
        while True:
            self.wn.update()
            if self.state == RUNNING:
                self._clear_overlay()
                self._tick()
            elif self.state == GAME_OVER:
                # mostrar overlay de game over y esperar R o Esc
                self._overlay_text("GAME OVER - Presiona R para reiniciar")
            time.sleep(self.delay)

    # ---------------- Lógica por tick ----------------
    def _tick(self):
        # Mover
        self.snake.move()

        # Colisiones con borde
        x, y = self.snake.head.position()
        if (x > WIDTH//2 - STEP or x < -WIDTH//2 + STEP or
            y > HEIGHT//2 - STEP or y < -HEIGHT//2 + STEP):
            self.state = GAME_OVER
            return

        # Colisión con cuerpo
        if self.snake.hits_itself():
            self.state = GAME_OVER
            return

        # Comida
        if self.snake.head.distance(self.food.t) < STEP - 5:
            self.snake.grow()
            self.food.place_away_from(self.snake.occupied_positions())
            self.score.increment()
            self._speedup_if_needed()

        # Redibujar marcador
        self.score.draw()

