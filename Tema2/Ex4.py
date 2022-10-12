# Iacob Andrei - 3E4
# Homework 2, Ex4 ML from Lab2-Exercises

import matplotlib.pyplot as plt
from itertools import product
from tools.stats import probability_weighted, WeightedOutcome
from dataclasses import dataclass


# Exercise 4
# Let S be the outcome of a random variable describing the sum of two dice thrown independently.

# 1. Print the probability distribution of $S$ graphically.

def ex4():

    @dataclass(frozen=True)
    class Outcome(WeightedOutcome):
        die_sum: int

    def pmf(X, a, omega):
        A = set(o for o in omega if X[o.die_sum] is a)
        return probability_weighted(A, omega)

    omega = []
    S = list(o[0] + o[1] for o in product(range(1, 7), range(1, 7)))
    X = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}
    k = sorted(set(X.values()))

    for sum in k:
        omega.append(Outcome(die_sum=sum, weight=S.count(sum)))

    pmf_X = [pmf(X, x, omega) for x in k]

    fig, ax = plt.subplots(1, 1)
    ax.bar(k, pmf_X)
    plt.ylabel("pmf")
    plt.xlabel("k")
    plt.title("Probability mass function")
    plt.show()

    # 2. Determine $E[S]$ and $Var(S)$.

    E_S = 0
    Var_S = 0
    for i, ki in enumerate(k):
        E_S += k[i] * pmf_X[i]

    for i, ki in enumerate(k):
        Var_S += (ki - E_S) ** 2 * pmf_X[i]

    print("E[S] =", E_S)
    print("Var[S] = ", Var_S)


if __name__ == "__main__":
    ex4()