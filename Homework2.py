#Iacob Andrei - 3E4
#Homework 2 ML from Lab2-Exercises


import matplotlib.pyplot as plt
from scipy.stats import binom 
from scipy.stats import geom
from itertools import product
from tools.stats import probability_weighted, WeightedOutcome
from dataclasses import dataclass

# Exercise 1
# Give an example of a a real phenomenon modelled by the following discrete distributions and plot an illustrative pmf for that phenomenon using `matplotlib` and `scipy.stats` functions:

# 1. binomial;

# Experiment: Probability for a bakery of sell K bagels when having n customers in a day, knowing that the probability of selling a bagel is p.

# n = 50 # number of customers
# p = 0.70 # probability of selling a baggel
# k = range(0, 50) # number of sold baggels in a day

# pmf_X = binom.pmf(k, n, p)

# fig, ax = plt.subplots(1, 1)
# ax.bar(k, pmf_X)
# plt.ylabel("pmf")
# plt.xlabel("k")
# plt.title("Probability mass function")
# plt.show()

# From the graphic, we can say that the highest number of sold bagels is around 35, out of 50 customers, with a probability of around 12%

# 2. geometric.

# Experiment: A goalkeeper trains. The probability that he save a penalty is 20%. Using the geometric distribution we can visualise the probability of him saving x shots.

# p = 0.2
# X = range(1,11,1)

# geom_pd = geom.pmf(X, p)

# fig, ax = plt.subplots(1, 1)
# ax.bar(X, geom_pd)
# plt.ylabel("pmf")
# plt.xlabel("x")
# plt.title("Probability mass function")
# plt.show()

# From the graphic, we can say that the probability to save 1/10 shots is 20%, the probabilty of saving 6/10 shots is around 5% and the probability of saving 10/10 shots is around 2.5%




# Exercise 4
# Let S be the outcome of a random variable describing the sum of two dice thrown independently.

# 1. Print the probability distribution of $S$ graphically.

# @dataclass(frozen=True)
# class Outcome(WeightedOutcome):
#     die_sum : int

# def pmf(X, a, omega):
#     A = set(o for o in omega if X[o.die_sum] is a)
#     return probability_weighted(A, omega)

# omega = []
# S = list(o[0] + o[1] for o in product(range(1,7), range(1,7)))
# X = { 2: 2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12}
# k = sorted(set(X.values()))

# for sum in k:
#     omega.append( Outcome(die_sum=sum, weight=S.count(sum)) )

# pmf_X = [pmf(X, x, omega) for x in k]

# fig, ax = plt.subplots(1, 1)
# ax.bar(k, pmf_X)
# plt.ylabel("pmf")
# plt.xlabel("k")
# plt.title("Probability mass function")
# plt.show()

# 2. Determine $E[S]$ and $Var(S)$.

# E_S = 0
# Var_S = 0

# for i,ki in enumerate(k):
#     E_S +=  k[i] * pmf_X[i]

# for i, ki in enumerate(k):
#     Var_S += (ki-E_S)**2 * pmf_X[i]

# print("E[S] =",E_S)
# print("Var[S] = ", Var_S)



# Exercise 6
# A sailor is trying to walk on a slippery deck, but because of the movements of the ship, he can make exactly one step every second, either forward (with probability $p=0.5$) or backward (with probability $1-p=0.5$). Using the `scipy.stats.binom` package, determine the probability that the sailor is in position +8 after 16 seconds.

p = 0.5
n = 16
k = range(0,17)

pmf_X = binom.pmf(k, n, p)

fig, ax = plt.subplots(1, 1)
ax.bar(k, pmf_X)
plt.ylabel("pmf")
plt.xlabel("k")
plt.title("Probability mass function")
# plt.show()

for i, prob in enumerate(pmf_X):
    print(f"Probabilitatea de a merge in fata {i} pasi. Pozitia {i - (16-i)}. Prob = {prob}")

# pentru a ajunge pe pozitia +8, este nevoie de 12 pasi in fata, si 4 inapoi
print(pmf_X[12])