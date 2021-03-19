# Diego Esparza Hurtado           A01652327
# Edgar Federico González Aguirre A01383154

# Se importan las librerías necesarias:
from random import randrange
from turtle import *
from freegames import vector

# Se crean los oobjetos necesarios para que funcione el código.
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Método para responder al clic en el programa.
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10

# Método para checar si el objeto se encuentra dentro del marco del juego.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Método para dibujar la pelota y los blancos.
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Método para mover las pelotas.
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.7

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

# Lo objetivos que ya no se encuentran en la pantalla, se reposicionan en el extremo derecho de la pantalla con la misma altura que tenían previamente.
    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

# Se inicia el entorno del juego.
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()