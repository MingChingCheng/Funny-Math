# Elementary cellular automaton

## Cellular automaton

- Like a step by step animation
- All cells are located on a grid
- Each cell has different state, usually use different color to represent
- The state is depending on the neighbors.

## Introduction

The Elementary cellular automaton use 3 cells in previous row to generate 1 cell in next row.
The total states of 3 cells can be following pattern:

| 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |

Total 8 patterns as shown above.
We can define different results for each pattern, for example:

| 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  1  |  1  |  0  |  0  |  1  |  0  |  1  |  0  |

Since the '11001010' in decimal number is '202', this rule is called "Rule 202"
See [Wolfram code](https://en.wikipedia.org/wiki/Wolfram_code)

## Rule 90

In Rule 90, only the neighbors in previous line will influence the result.
Also based on XOR function.

| 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |  1  |  0  |  1  |  1  |  0  |  1  |  0  |

## Rule 184

Rule 184 can be used in traffic simulation.
If the front of car is empty, than car can move forward.
If the front of car is occupied by other, than car stuck in original place.

| 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  1  |  0  |  1  |  1  |  1  |  0  |  0  |  0  |

## In Natural

Conus textile has a special shell with cellular automata
[Picture](https://en.wikipedia.org/wiki/File:Textile_cone.JPG)

## Reference

- [Stephan Wolfram - A New Kind of Science](https://www.wolframscience.com/nks/)
- [Wiki - Elementary_cellular_automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton)

## Other different cellular automata

- [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant)
- [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Lenia](https://en.wikipedia.org/wiki/Lenia)
