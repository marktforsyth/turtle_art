from turtle import *  # TODO: try out the Rust turtle crate
from math import sqrt, cos, sin, pi, degrees
from random import random


def square(radius, theta):
    x = radius * cos(theta + pi / 4)
    y = radius * sin(theta + pi / 4)

    penup()
    goto(x, y)
    setheading(3 * pi / 2 + theta)
    pendown()

    for _ in range(4):
        forward(sqrt(2 * radius**2))
        right(pi / 2)


def main():
    radians()
    speed(0)
    bgcolor(0.1, 0.1, 0.1)
    hideturtle()

    ITERATIONS = 10
    STEP = pi / 2 / ITERATIONS

    radius = 300
    thickness = abs(radius - 0.5 * sqrt(2 * radius**2))

    for _ in range(6):
        for t in range(ITERATIONS):
            pencolor(0.6 * random() + 0.4, 0.6 * random() + 0.4, 0.6 * random() + 0.4)
            square(radius, t * STEP)

        radius -= thickness
        thickness = abs(radius - 0.5 * sqrt(2 * radius**2))

    done()


if __name__ == '__main__':
    main()
