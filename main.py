import pgzrun
import random

#type: ignore[screen]

WIDTH, HEIGHT = 1400, 800  
maxRadius = 20  
minRadius = 1   
sensitiveArea = 40  

mouse = {"xPos": 0, "yPos": 0}

colorArray = [
    (240, 248, 255), (250, 235, 215), (0, 255, 255), (127, 255, 212), (240, 255, 255), 
    (245, 245, 220), (255, 228, 196), (0, 0, 0), (255, 235, 205), (0, 0, 255), 
    (138, 43, 226), (165, 42, 42), (222, 184, 135), (95, 158, 160), (127, 255, 0), 
    (210, 105, 30), (255, 127, 80), (100, 149, 237), (255, 248, 220), (220, 20, 60), 
    (0, 255, 255), (0, 0, 139), (0, 139, 139), (184, 134, 11), (169, 169, 169), 
    (0, 100, 0), (189, 183, 107), (139, 0, 139), (85, 107, 47), (255, 140, 0), 
    (153, 50, 204), (139, 0, 0), (233, 150, 122), (143, 188, 143), (72, 61, 139), 
    (47, 79, 79), (0, 206, 209), (148, 0, 211), (255, 20, 147), (0, 191, 255)
]

class Circle:
    def __init__(self, xPos, yPos, dx, dy, radius):
        self.xPos = xPos
        self.yPos = yPos
        self.dx = dx
        self.dy = dy
        self.radius = minRadius 
        self.color = random.choice(colorArray)

    def draw(self):
        screen.draw.filled_circle((self.xPos, self.yPos), self.radius, self.color)

    def update(self):
        if self.xPos + self.radius > WIDTH or self.xPos - self.radius < 0:
            self.dx *= -1
        if self.yPos + self.radius > HEIGHT or self.yPos - self.radius < 0:
            self.dy *= -1

        self.xPos += self.dx
        self.yPos += self.dy

        if (
            abs(mouse["xPos"] - self.xPos) < sensitiveArea and
            abs(mouse["yPos"] - self.yPos) < sensitiveArea and
            self.radius < maxRadius
        ):
            self.radius += 1
        elif self.radius > minRadius:
            self.radius -= 0.2

circleArray = []
for _ in range(3000): 
    radius = random.uniform(5, 10)  
    xPos = random.uniform(radius, WIDTH - radius)
    yPos = random.uniform(radius, HEIGHT - radius)
    dx = random.uniform(-3, 3)
    dy = random.uniform(-3, 3)
    circleArray.append(Circle(xPos, yPos, dx, dy, radius))


def draw():
    screen.clear()
    for circle in circleArray:
        circle.draw()


def update():
    for circle in circleArray:
        circle.update()


def on_mouse_move(pos):
    mouse["xPos"], mouse["yPos"] = pos


pgzrun.go()