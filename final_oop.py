import turtle
import random


class Ball:
    def __init__(self, color, size, i, xpos, ypos, vx, vy, dt, canvas_width, canvas_height, ball_radius):
        self.color = color
        self.size = size
        self.i = i
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.dt = dt
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius

    def draw_ball(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.xpos, self.ypos - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self):
        self.xpos += self.vx * self.dt
        self.ypos += self.vy * self.dt

    def update_ball_velocity(self):
        if abs(self.xpos) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx
        if abs(self.ypos) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy


class RunBall:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.ball_list = []
        dt = 0.2

        for i in range(self.num_balls):
            self.xpos = (random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos = (random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx = (10 * random.uniform(-1.0, 1.0))
            self.vy = (10 * random.uniform(-1.0, 1.0))
            self.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(Ball(self.ball_color, self.ball_radius, i, self.xpos, self.ypos, self.vx, self.vy, dt, self.canvas_width, self.canvas_height, self.ball_radius))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step
        while (True):
            turtle.clear()
            self.draw_border()
            for i in range(self.num_balls):
                ball = Ball(self.ball_color, self.ball_radius, i, self.xpos, self.ypos, self.vx, self.vy, dt, self.canvas_width, self.canvas_height, self.ball_radius)
                ball.draw_ball()
                ball.move_ball()
                ball.update_ball_velocity()
            turtle.update()
        turtle.done()


ball_run = RunBall()
ball_run.run()


class SevenSegments:
    def __init__(self, digit):
        self.color = (255, 0, 0)
        self.digit = digit
        self.dt = 0.2

        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        turtle.color(self.color)
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(0, 0)
        turtle.pensize(10)

    def draw(self):
        if self.digit == 0:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.penup()

        if self.digit == 1:
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

        if self.digit == 2:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.penup()

        if self.digit == 3:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()

        if self.digit == 4:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.penup()

        if self.digit == 5:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()

        if self.digit == 6:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

        if self.digit == 7:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

        if self.digit == 8:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.penup()
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()

        if self.digit == 9:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

    def clear(self):
        turtle.clear()

    def my_delay(self):
        import time
        start = time.time()
        while time.time() - start < self.dt:
            pass

    def run(self):
        while True:
            for i in range(0, 10):
                self.clear()
                self.draw()
                self.my_delay()
                turtle.update()
        turtle.done()


for i in range(0, 10):
    num_run = SevenSegments(i)
    num_run.run()
