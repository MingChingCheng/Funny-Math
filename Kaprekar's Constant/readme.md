# Kaprekar's constant

Kaprekar's routine is an iterative algorithm, invented by an Indian mathematician D. R. Kaprekar.

Rule:

1. Pick a number, $n_0$
2. Sort $n_0$ into descending order, than get $a$
3. Sort $n_0$ into ascending order, than get $b$
4. Calculate $a - b$, than get a new number, $n_1$
5. Repeat step 1 ~ step 4, until $n_x$ become stable, the number of iterations is called "Kaprekar's constant"

Example:

1. Pick 6594
2. Do the algorithm
    iteration 1 : 9654 - 4569 = 5085
    iteration 2 : 8550 - 558 = 7992
    iteration 3 : 9972 - 2799 = 7173
    iteration 4 : 7731 - 1377 = 6354
    iteration 5 : 6543 - 3456 = 3087
    iteration 6 : 8730 - 378 = 8352
    iteration 7 : 8532 - 2358 = 6174
    iteration 8 : 7641 - 1467 = 6174
3. Take 7 iterations to reach a constant
