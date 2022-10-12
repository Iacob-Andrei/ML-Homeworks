# Iacob Andrei - 3E4
# Homework 2, Ex1 ML from Lab2-Exercises

import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import geom


# Exercise 1 Give an example of a real phenomenon modelled by the following discrete distributions and plot an
# illustrative pmf for that phenomenon using `matplotlib` and `scipy.stats` functions:

# 1. binomial;

# Experiment: Probability for a bakery of sell K bagels when having n customers in a day, knowing that the
# probability of selling a bagel is p.

def sub_pct1():
    n = 50  # number of customers
    p = 0.70  # probability of selling a bagel
    k = range(0, 50)  # number of sold bagels in a day

    pmf_X = binom.pmf(k, n, p)

    fig, ax = plt.subplots(1, 1)
    ax.bar(k, pmf_X)
    plt.ylabel("pmf")
    plt.xlabel("k")
    plt.title("Probability mass function")
    plt.show()

    # From the graphic, we can say that the highest number of sold bagels is around 35, out of 50 customers,
    # with a probability of around 12%

    # 2. geometric.

    # Experiment: A goalkeeper trains. The probability that he save a penalty is 20%. Using the geometric
    # distribution we can visualise the probability of him saving x shots.


def sub_pct2():
    p = 0.2
    X = range(1, 11, 1)

    geom_pd = geom.pmf(X, p)

    fig, ax = plt.subplots(1, 1)
    ax.bar(X, geom_pd)
    plt.ylabel("pmf")
    plt.xlabel("x")
    plt.title("Probability mass function")
    plt.show()

    # From the graphic, we can say that the probability to save 1/10 shots is 20%, the probabilty of saving 6/10
    # shots is around 5% and the probability of saving 10/10 shots is around 2.5%


if __name__ == "__main__":
    sub_pct1()
    sub_pct2()
