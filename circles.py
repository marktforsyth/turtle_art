from turtle import *
from math import pi, cos, sin
from random import random


def concentric_circles(x, y, radius, count):
    for c in range(count):
        current_radius = radius / count * (c + 1)

        pencolor(0.5 * random() + 0.5, 0.5 * random() + 0.5, 0.5 * random() + 0.5)
        penup()
        goto(x, y - current_radius)
        pendown()

        circle(current_radius)


def main():
    radians()
    speed(0)
    bgcolor(0.1, 0.1, 0.1)
    hideturtle()
    pensize(2)

    LARGE_RADIUS = 200
    POINTS = 12

    for p in range(POINTS):
        x = LARGE_RADIUS * cos(pi / 2 + p * 2 * pi / POINTS)
        y = LARGE_RADIUS * sin(pi / 2 + p * 2 * pi / POINTS)

        concentric_circles(x, y, 120, 6)

    done()


if __name__ == '__main__':
    main()
