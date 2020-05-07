from normalcdf import normal_cdf
from cdfInverse import inverse_normal_cdf
import math
import random

def	normal_approximation_to_binomial(n,	p):				
    """finds	mu	and	sigma	corresponding	to	a	Binomial(n,	p)"""				
    mu = p*n				
    sigma = math.sqrt(p	* (1 - p) *	n)				
    return	mu,	sigma
#the normal	cdf	_is_ the probability	the	variable is	below a	threshold 
normal_probability_below	=	normal_cdf

#it's	above	the	threshold	if	it's	not	below	the	threshold 
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu=0,sigma=1)

#	it's	between	if	it's	less	than	hi,	but	not	less	than	lo
def  normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

#	it's	outside	if	it's	not	between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


#################### reversing ############################

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns	the	z	for	which	P(Z	<=	z)	=	probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns	the	z	for	which	P(Z	>=	z)	=	probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns	the	symmetric	(about	the	mean)	bounds
        that	contain	the	specified	probability"""
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)



#	95%	bounds	based	on	assumption	p	is	0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

#	actual	mu	and	sigma	based	on	p	=	0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

#	a	type	2	error	means	we	fail	to	reject	the	null	hypothesis 
#which	will	happen	when	X	is	still	in	our	original	interval

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 -  type_2_probability

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu : 
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_above(x, mu, sigma)

# simulation to make sure that two two_sided_p_value(529.5) work well
extreme_value_count = 0
for _ in range(100000):
    num_heads = sum( 1 if random.random() < 0.5  else 0 
                    for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count+=1
print( extreme_value_count / 100000)

