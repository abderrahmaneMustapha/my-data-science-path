#### Implementation of Cumulative distribution function for the standard normal distribution ####
import matplotlib.pyplot as plt
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x-mu) / math.sqrt(2) / sigma )) / 2

def plot():
    xs = [x / 10.0 for x in range(-50, 50)]


    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-,', label='mu=-1, sigma=1')
    plt.legend()
    plt.title("Various normal cdf")
    plt.show()