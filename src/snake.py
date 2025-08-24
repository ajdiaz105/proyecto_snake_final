
import turtle as t

class Segment:
    def __init__(self, x, y, color="white"):
        self.t = t.Turtle()
        self.t.speed(0)
        self.t.shape("square")
        self.t.color(color)
        self.t.penup()
        self.t.goto(x, y)

    def goto(self, x, y):
        self.t.goto(x, y)

    def position(self):
        return self.t.xcor(), self.t.ycor()

class Head(Segment):
    def __init__(self, x, y, color="white"):
        super().__init__(x, y, color)

    def setx(self, x): self.t.setx(x)
    def sety(self, y): self.t.sety(y)

    def distance(self, other_turtle):
        return self.t.distance(other_turtle)

class Snake:
    def __init__(self, step=20):
        self.step = step
        self.dx, self.dy = step, 0
        self.head = Head(0, 0, "white")
        self.body = []
        # cuerpo inicial
        for i in range(1, 3):
            self.body.append(Segment(-i*step, 0, "white"))

    def reset(self):
        # Mover todo fuera de pantalla y reconstruir
        self.head.goto(0, 0)
        self.dx, self.dy = self.step, 0
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body = []
        for i in range(1, 3):
            self.body.append(Segment(-i*self.step, 0, "white"))

    def set_direction(self, dx, dy):
        # evita reversa inmediata
        if (self.dx != 0 and dx != 0) or (self.dy != 0 and dy != 0):
            return
        # establece nueva dirección si es válida
        self.dx, self.dy = dx, dy

    def move(self):
        # mover cuerpo del final al principio
        for i in range(len(self.body)-1, 0, -1):
            x, y = self.body[i-1].position()
            self.body[i].goto(x, y)
        if self.body:
            xh, yh = self.head.position()
            self.body[0].goto(xh, yh)
        # mover cabeza
        self.head.setx(self.head.position()[0] + self.dx)
        self.head.sety(self.head.position()[1] + self.dy)

    def grow(self):
        # agrega segmento al final (en la última posición del último segmento)
        if self.body:
            x, y = self.body[-1].position()
        else:
            # si no hay cuerpo aún, agrega detrás de la cabeza
            x = self.head.position()[0] - self.dx
            y = self.head.position()[1] - self.dy
        self.body.append(Segment(x, y, "white"))

    def hits_itself(self):
        hx, hy = self.head.position()
        for seg in self.body:
            x, y = seg.position()
            if abs(hx - x) < self.step/2 and abs(hy - y) < self.step/2:
                return True
        return False

    def occupied_positions(self):
        # devuelve set de posiciones ocupadas en el grid
        occ = {tuple(map(int, self.head.position()))}
        for s in self.body:
            occ.add(tuple(map(int, s.position())))
        return occ
