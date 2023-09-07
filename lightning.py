from turtle import *
from math import pi
from random import randrange, uniform
from typing import TypeAlias, Final


End: TypeAlias = tuple[float, float, float]


def segment(x: float, y: float, orig_theta: float, pieces: int) -> End:
  penup()
  goto(x, y)
  pendown()

  for _ in range(pieces):
    setheading(orig_theta - pi / 4 + uniform(0, pi / 2))
    forward(10 + randrange(10))

  return pos()[0], pos()[1], heading()


def fork(end: End, level: int) -> tuple[End, End]:
  fork_one: Final[End] = segment(
    end[0],
    end[1],
    end[2] + uniform(pi / 12, pi / 6),
    20 - level * randrange(3, 6)
  )
  fork_two: Final[End] = segment(
    end[0],
    end[1],
    end[2] - uniform(pi / 12, pi / 6),
    20 - level * randrange(2, 3)
  )

  return fork_one, fork_two


def lightning(path_ends: tuple[End, ...], level: int) -> None:
  if level == 0:
    path_end: Final[End] = segment(-300, 300, 7 * pi / 4, 15 + randrange(10))

    lightning((path_end,), 1)

  continuing_ends: Final[tuple[End, ...]] = tuple(end for end in path_ends if randrange(99) > 9 + 20 * level)
  new_forks: Final[tuple[tuple[End, End], ...]] = tuple(
    map(
      fork,
      continuing_ends,
      tuple(level for _ in continuing_ends)
    )
  )
  new_ends: Final[tuple[End, ...]] = tuple(fork[0] for fork in new_forks) + tuple(fork[1] for fork in new_forks)

  if len(new_ends) > 0:
    lightning(new_ends, level + 1)
  elif level == 1:
    segment(pos()[0], pos()[1], 7 * pi / 4, 25 + randrange(10))


def main():
  title('Lightning')
  radians()
  width(2)
  bgcolor(0.1, 0.1, 0.1)
  pencolor(0.8, 0.8, 0.8)
  speed(10)

  lightning([], 0)

  hideturtle()
  mainloop()


if __name__ == '__main__':
  main()
