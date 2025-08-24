
import turtle as t

class Score:
    def __init__(self, width, height):
        self.value = 0
        self.high = 0  # si quieres persistir, guarda/lee de archivo
        self.pen = t.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, height//2 - 30)

        # Segundo lapicero para overlays (pausa/game over)
        self.pen2 = t.Turtle()
        self.pen2.hideturtle()
        self.pen2.speed(0)
        self.pen2.color("white")
        self.pen2.penup()

        self.draw()

    def increment(self):
        self.value += 1
        if self.value > self.high:
            self.high = self.value
        self.draw()

    def reset(self):
        self.value = 0
        self.draw()
        self.pen2.clear()

    def draw(self):
        self.pen.clear()
        self.pen.write(f"SCORE: {self.value}   HIGH: {self.high}", align="center", font=("Courier", 16, "normal"))
