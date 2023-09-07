from turtle import *
from math import pi, sin, cos


def flower(petals, radius):
  for p in range(petals):
    x = radius * cos(2 * pi / petals * p)
    y = radius * sin(2 * pi / petals * p) - radius

    penup()
    goto(x, y)
    pendown()

    circle(radius)


def main():
  radians()
  speed(9)
  shape('arrow')
  bgcolor(0.1, 0.1, 0.1)
  pencolor(0.8, 0.8, 0.8)

  flower(7, 150)

  hideturtle()
  done()


if __name__ == '__main__':
  main()

