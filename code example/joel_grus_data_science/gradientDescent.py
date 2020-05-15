import matplotlib.pyplot as plt
from functools import partial
import random
# Gradient Descent implemenataion 

def sum_of_squares(v):
    """ computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h ) - f(x)) / h


#example of quare function and the derivative

def square(x):
    return x * x 

def derivative(x):
    return 2 * x

# estimate the derivative vs real  derivative

derivative_estimate = partial(difference_quotient, square,h=0.00001)

x =  range(-10,10)
plt.title('Actual Derivations vs Estimates')
plt.plot(x, list(map(derivative, x)), '-', label='Actual')
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label='Estiamte')
plt.legend(loc=9)
plt.show()

def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j==i else 0)
        for j, v_j in enumerate(v)]
    return (f(w) - f(v) ) / h

def estimate_gradient(f, v, h=0.00001):
    return [ partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]

# Using the Gradient
def step(v, direction, step_size):
    """ move step size in the direction from v """
    return [v_i + step_size * direction
           for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [ 2 * v_i for v_i in v]

# pick a random starting point
v = [ random.randint(-10, 10) for i in range(3)]
tolerance =	0.0000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

def safe(f):
    """return	a	new	function	that's	the	same	as	f,				
      except that it outputs	infinity	whenever f produces	an	error"""
    def safe_f(*args, **kwargs):
        try : 
            return f(*args, **kwargs)
        except:
            return float('inf')
        return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    step_sizes	=	[100,	10,	1,	0.1,	0.01,	0.001,	0.0001,	0.00001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

        #choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        	#	stop	if	we're	"converging"
        if	abs(value	-	next_value)	<	tolerance:
            return	theta								
        else:	 											
            theta, value =	next_theta,	next_value

def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)
def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]
def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
    negate_all(gradient_fn),
    theta_0,
    tolerance)



         
