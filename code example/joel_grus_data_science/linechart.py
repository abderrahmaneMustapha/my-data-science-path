import matplotlib.pylab as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [ x + y for x, y in zip(variance, bias_squared)]
xs = [i  for i,_ in  enumerate(variance)]

plt.plot(xs,     variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs,  total_error, 'b:', label='total error')

plt.legend(loc=9)
plt.xlabel('model copmlexity')
plt.title('The Bias-Variance Tradeoff')
plt.show()