"""
================================================
   Mandala Pattern Generator — Python Turtle
   Draws 5 different colorful mandala patterns
================================================
"""

import turtle
import colorsys

# ── Setup ──────────────────────────────────────
screen = turtle.Screen()
screen.title("🌸 Mandala Pattern Generator")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)          # Turn off animation for speed

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)


# ── Utility ────────────────────────────────────
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def set_color_hsv(hue, saturation=0.9, value=1.0):
    r, g, b = colorsys.hsv_to_rgb(hue % 1.0, saturation, value)
    t.pencolor(r, g, b)


# ── Pattern 1: Classic Petal Mandala ───────────
def petal_mandala(petals=36, size=180):
    print("Drawing Pattern 1: Petal Mandala...")
    clear()
    t.penup(); t.goto(0, 0); t.pendown()

    for i in range(petals):
        hue = i / petals
        set_color_hsv(hue)
        t.circle(size, 60)
        t.left(60)
        t.circle(size, 60)
        t.left(360 / petals - 120)

    screen.update()


# ──Pattern 2: Star Burst Mandala ──────────────
def starburst_mandala(spokes=72, length=300):
    print("Drawing Pattern 2: Star Burst Mandala...")
    clear()

    for i in range(spokes):
        hue = i / spokes
        set_color_hsv(hue)
        t.penup(); t.goto(0, 0); t.pendown()
        angle = i * (360 / spokes)
        t.setheading(angle)
        t.forward(length * 0.2)
        # Draw a small petal along each spoke
        for _ in range(2):
            t.circle(length * 0.4, 60)
            t.left(120)
        t.forward(length * 0.2)

    screen.update()


# ── Pattern 3: Spiral Mandala ──────────────────
def spiral_mandala(loops=6, sides=8):
    print("Drawing Pattern 3: Spiral Mandala...")
    clear()
    t.penup(); t.goto(0, 0); t.pendown()

    step = 5
    length = 5
    angle = 360 / sides

    for i in range(loops * sides * 10):
        hue = (i / (loops * sides * 10))
        set_color_hsv(hue)
        t.forward(length)
        t.right(angle + 1)          # slight extra turn creates spiral
        length += step / (sides * 3)

    screen.update()


# ── Pattern 4: Rose / Rhodonea Mandala ─────────
def rose_mandala(petals=8, size=300):
    print("Drawing Pattern 4: Rose Mandala...")
    clear()

    steps = 1000
    import math

    for k in range(2):                 # draw twice for inner + outer
        scale = size * (0.5 + 0.5 * k)
        for i in range(steps + 1):
            theta = math.radians(i * 360 / steps)
            r = scale * math.cos(petals * theta)
            x = r * math.cos(theta)
            y = r * math.sin(theta)

            hue = i / steps
            set_color_hsv(hue, 0.8, 1.0)

            if i == 0:
                t.penup(); t.goto(x, y); t.pendown()
            else:
                t.goto(x, y)

    screen.update()


# ── Pattern 5: Layered Circle Mandala ────────
def layered_mandala(layers=12, base_radius=20):
    print("Drawing Pattern 5: Layered Circle Mandala...")
    clear()

    for layer in range(layers):
        hue = layer / layers
        radius = base_radius + layer * 22
        circles = 6 + layer * 2       # more circles as layer grows
        set_color_hsv(hue)

        for i in range(circles):
            angle = i * (360 / circles)
            x = radius * __import__('math').cos(__import__('math').radians(angle))
            y = radius * __import__('math').sin(__import__('math').radians(angle))
            t.penup(); t.goto(x, y - base_radius); t.pendown()
            t.circle(base_radius)

    screen.update()


# ── Menu ───────────────────────────────────
def show_menu():
    """Draw clickable text menu on screen."""
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.color("white")

    labels = [
        (0,  350, "🌸 Mandala Pattern Generator — Click a number key!"),
        (0,  310, "Press  1  →  Petal Mandala"),
        (0,  280, "Press  2  →  Star Burst Mandala"),
        (0,  250, "Press  3  →  Spiral Mandala"),
        (0,  220, "Press  4  →  Rose Mandala"),
        (0,  190, "Press  5  →  Layered Circle Mandala"),
        (0, -350, "Press  Q  to Quit"),
    ]
    for (x, y, text) in labels:
        menu.goto(x, y)
        menu.write(text, align="center", font=("Arial", 13, "bold"))

    screen.update()
    return menu


# ── Key Bindings ───────────────────────────────
patterns = {
    "1": petal_mandala,
    "2": starburst_mandala,
    "3": spiral_mandala,
    "4": rose_mandala,
    "5": layered_mandala,
}

menu_turtle = show_menu()

def on_key(pattern_fn):
    def handler():
        menu_turtle.clear()
        pattern_fn()
        # Re-show hint at bottom
        menu_turtle.penup()
        menu_turtle.color("gray")
        menu_turtle.goto(0, -360)
        menu_turtle.write("Press 1–5 for another pattern | Q to Quit",
                          align="center", font=("Arial", 11, "normal"))
        screen.update()
    return handler

for key, fn in patterns.items():
    screen.onkey(on_key(fn), key)

screen.onkey(lambda: turtle.bye(), "q")
screen.onkey(lambda: turtle.bye(), "Q")

screen.listen()

# Draw pattern 1 automatically on start
on_key(petal_mandala)()

turtle.mainloop()
