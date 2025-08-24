
import turtle as t
import random

class Food:
    def __init__(self, width, height, step):
        self.width, self.height, self.step = width, height, step
        self.t = t.Turtle()
        self.t.speed(0)
        self.t.shape("square")   # retro: cuadrado
        self.t.color("white")    # monocromo
        self.t.penup()
        self.t.goto(0, step*5)

    def _random_grid_coord(self):
        x = random.randrange(-self.width//2 + self.step, self.width//2 - self.step, self.step)
        y = random.randrange(-self.height//2 + self.step, self.height//2 - self.step, self.step)
        return x, y

    def place_away_from(self, occupied_positions):
        # intenta ubicar la comida fuera de la serpiente
        for _ in range(1000):
            x, y = self._random_grid_coord()
            if (int(x), int(y)) not in occupied_positions:
                self.t.goto(x, y)
                return
        # fallback improbable
        self.t.goto(0, 0)
