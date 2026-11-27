# Elementary cellular automaton

## Cellular automaton

- Like a step by step animation
- All cells are located on a grid
- Each cell has different state, usually use different color to represent
- The state is depending on the neighbors.

## Introduction

First introduced by Christopher Gale Langton in 1986.
This game has a 2D board and one ant.
The ant will "turn direction", "change color", and "move forward" depends on the state or color of the board.
This kind of system also called: "Turmite" or "Turning machine"

- In beginning, it will generate a symmetric pattern.
- After more steps, it seems like a chaotic, random behavior.
- After about 10000 steps, a "high way" pattern of 104 steps will repeat forever.

## Basic Rule

- At white square:
  - turn right
  - flip the color
  - move forward
- At black square:
  - turn left
  - flip the color
  - move forward

## Advanced Rule

We can use more colors or play on a square/hexagonal board
The colors are modified in a cyclic fashion.
Use letters to indicate turning direction.

For square board

- "L" >> Left (turn 90 degree)
- "R" >> Right (turn -90 degree)
- "U" >> U-turn (turn 180 degree)

For hexagonal board

- "N" >> no change
- "L1" >> turn 60 degree
- "L2" >> turn 120 degree
- "U" >> turn 180 degree
- "R2" >> turn 240 degree
- "R1" >> turn 300 degree

By the above rules, we can name the basic rule as "RL"
More examples:
[LLRR](https://en.wikipedia.org/wiki/File:LangtonsAnt-nColor_LLRR_123157.png): Grows symmetrically
[LRRRRRLLR](https://en.wikipedia.org/wiki/File:LangtonsAnt-nColor_LRRRRRLLR_70273.png): Fills space in a square around itself.
[R1R2NUR2R1L2](https://en.wikipedia.org/wiki/File:CA50338_animation.gif): example in hexagonal board.

## Other Termite

- [Turmite](https://en.wikipedia.org/wiki/Turmite)
- [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant)
- [Paterson's worm](https://en.wikipedia.org/wiki/Paterson's_worms)
