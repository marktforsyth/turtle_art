from turtle import *
from math import pi
from random import random


def line_star(radius, sides, tilted=False):
    for s in range(sides):
        penup()
        goto(0, 0)
        pendown()

        optional_tilt = 0
        if tilted:
            optional_tilt = pi / sides

        setheading(2 * pi * s / sides + pi / 2 + optional_tilt)
        forward(radius)


def main():
    radians()
    speed(6)
    bgcolor(0.1, 0.1, 0.1)
    shape('arrow')

    CYCLES = 5
    BASE_RADIUS = 70
    RADIUS_INCR = 40
    LEAST_SIDES = 5

    pencolor(0.5 * random() + 0.5, 0.5 * random() + 0.5, 0.5 * random() + 0.5)
    line_star(BASE_RADIUS + RADIUS_INCR * CYCLES, LEAST_SIDES)

    for i in range(CYCLES - 1, 0, -1):
        pencolor(0.5 * random() + 0.5, 0.5 * random() + 0.5, 0.5 * random() + 0.5)
        line_star(BASE_RADIUS + RADIUS_INCR * i, LEAST_SIDES * 2**(CYCLES - 1 - i), True)

    hideturtle()
    done()


if __name__ == '__main__':
    main()
