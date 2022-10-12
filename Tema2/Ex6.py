# Iacob Andrei - 3E4
# Homework 2, Ex6 ML from Lab2-Exercises


import matplotlib.pyplot as plt
from scipy.stats import binom

# Exercise 6 A sailor is trying to walk on a slippery deck, but because of the movements of the ship, he can make
# exactly one step every second, either forward (with probability $p=0.5$) or backward (with probability
# $1-p=0.5$). Using the `scipy.stats.binom` package, determine the probability that the sailor is in position +8
# after 16 seconds.


def ex6():
    p = 0.5
    n = 16
    k = range(0, 17)

    pmf_X = binom.pmf(k, n, p)

    fig, ax = plt.subplots(1, 1)
    ax.bar(k, pmf_X)
    plt.ylabel("pmf")
    plt.xlabel("k")
    plt.title("Probability mass function")
    plt.show()

    for i, prob in enumerate(pmf_X):
        print(f"Probabilitatea de a merge in fata {i} pasi. Pozitia {i - (16-i)}. Prob = {prob}")

    # pentru a ajunge pe pozitia +8, este nevoie de 12 pasi in fata, si 4 inapoi
    print(pmf_X[12])


if __name__ == "__main__":
    ex6()
