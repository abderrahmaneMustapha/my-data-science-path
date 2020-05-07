# Joel_Grus Data Science from Scratch First Princ Notes
> my notes when i was reading this book

## Notes
### Chapter 01
#### Network metric degree : 
> we had a dict of employee and graph representing the  freindship data what we did is to calculate the for each  employee the number of freinds (network metric degree
centrality)
### Chapter 02
#### Back slash
>backslash to indicate that a statement continues onto the next line
#### Similar to list and faster 
> set() make containe only unique elements

#### Empty lists 
> all return true when all the elements of lists is true$
> any return true when atleast one element  is true

#### Sort lists : 
>Sorted is similar to sort

```python
# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
key=lambda (word, count): count,
reverse=True)
```

#### List Comprehension
##### examples
>and later fors can use the results of earlier ones:
```python
increasing_pairs = [(x, y) # only pairs with x < y,
for x in range(10) # range(lo, hi) equals
for y in range(x + 1, 10)]
```
#### iterators
> we use them with large list example : lazy_range

#### Random
> random.shuffle randomly reorders the elements of a list example :
``` python 
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten
# [2, 5, 1, 9, 7, 3, 8, 6, 4, 0] (your results will probably be different)

```

> random.randrange, which takes either 1 or 2 arguments and returns
an element chosen randomly from the corresponding range() example :
``` python
random.randrange(10) # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6) # choose randomly from range(3, 6) = [3, 4, 5]
```

>randomly choose a sample of elements without replacement (i.e., with
no duplicates), you can use random.sample example :  
```python
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]
```

#### Functional Tools
> use filter and partial to create function
```python
def is_even(x):
"""True if x is even, False if x is odd"""
return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]
```

> how to use map 
```python
def double(x):
return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs) # same as above
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]
```

>or
```python
def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
```

#### Enumerate
> The Pythonic solution is enumerate, which produces tuples (index, element):

```python
for i, document in enumerate(documents):
do_something(i, document)
```

>Similarly, if we just want the indexes:

```python
for i, _ in enumerate(documents): do_something(i) # Pythonic
```

### Chapter 03
#### Bar Charts
>a good choice when you want to show how some quantity varies among
some discrete set of items
#### Line Chats 
> a good choice for showing trends
#### Scatter
>right choice for visualizing the relationship between two paired sets of
data.
### Chapter 05
#### Median
> if we have n data point and the median is e if we add a new point b 
so the median will increase by a/b
```python
def median(v):
"""finds the 'middle-most' value of v"""
n = len(v)
sorted_v = sorted(v)
midpoint = n // 2
if n % 2 == 1:
# if odd, return the middle value
return sorted_v[midpoint]
else:
# if even, return the average of the middle values
lo = midpoint - 1
hi = midpoint
return (sorted_v[lo] + sorted_v[hi]) / 2
median(num_friends) # 6.0
```
#### Dispersion
>how spread out our data is
##### difference between the largest and smallest elements:
```python
# "range" already means something in Python, so we'll use a different name
def data_range(x):
return max(x) - min(x)
data_range(num_friends) # 99
```
##### variance:

```python
def de_mean(x):
"""translate x by subtracting its mean (so the result has mean 0)"""
x_bar = mean(x)
return [x_i - x_bar for x_i in x]
def variance(x):
"""assumes x has at least two elements"""
n = len(x)
deviations = de_mean(x)
return sum_of_squares(deviations) / (n - 1)
```

##### covariance:
```python
def covariance(x, y):
n = len(x)
return dot(de_mean(x), de_mean(y)) / (n - 1)
covariance(num_friends, daily_minutes) # 22.43
```
##### correlation
>The correlation is unitless and always lies between -1 (perfect anti-correlation) and 1
(perfect correlation).
```python
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
```

##### standard deviation
```python
def standard_deviation(x):
return math.sqrt(variance(x))
standard_deviation(num_friends) # 9.03
```
### Chapter 06
#### Conditional Probability
>When two events E and F are independent, then by definition we have:
>P( E, F) = P(E)P(F)

>If they are not necessarily independent (and if the probability of F is not zero), then we
define the probability of E “conditional on F” as:

> 1)  P( E | F) = P(E, F) / P(F)

>  We often rewrite this as

> 2) P(E , F) = P( E | F ) P(F)

>When E and F are independent, you can check that this gives:

>   P( E | F) = P(E)

##### Bayes’s Theorem
> P (E | F) = P( E, F) / P(F) = P(F | E) P(E) / P(F)

>the event F can be split into:

>P(F) = P(F | E) + P(F | non E)

>so that:

> P (E | F) P(F | E) P(E) / [ P(F | E ) P(E)  +  P(F | non E) P(non E)]

##### More 
> dont forget about continues distribution and the random one

>Normal distribution is important too  :  sigma is where bell is centerred and mu is the mean (how wide)
```python
def normal_pdf(x, mu=0, sigma=1):
sqrt_two_pi = math.sqrt(2 * math.pi)
return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

```

> when mu = 0  and sigma = 1 its called the standar normal distribution

```python
X = sigma Z + mu
so that :
Z = (X - mu ) / sigma
```
> find the value corresponding to a specified probability by doing a 
binary search beacause we can not calculate cdf fucntion inverse

```python 
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
"""find approximate inverse using binary search"""
# if not standard, compute standard and rescale
if mu != 0 or sigma != 1:
return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
hi_z, hi_p = 10.0, 1 # normal_cdf(10) is (very close to) 1
while hi_z - low_z > tolerance:
mid_z = (low_z + hi_z) / 2 # consider the midpoint
mid_p = normal_cdf(mid_z) # and the cdf's value there
if mid_p < p:
# midpoint is still too low, search above it
low_z, low_p = mid_z, mid_p
elif mid_p > p:
# midpoint is still too high, search below it
hi_z, hi_p = mid_z, mid_p
else:
break
return mid_z
```

##### The Central Limit Theorem
> a random variable defined as the average of a large number of independent
and identically distributed random variables is itself approximately normally distributed :
with mean 0 and standard deviation 1.

> Binomial(n,p) random variable  : is a sum of "n"  independent  bernouli(p) variable
 read more on page 125 about bernouli and binomial and their standar variation and mean
``` python 
def bernoulli_trial(p):
return 1 if random.random() < p else 0
```

``` python 
def binomial(n, p):
return sum(bernoulli_trial(p) for _ in range(n))
```
### Chapter 07 
#### Statistical	Hypothesis	Testing
> we’ll	want	to	test	whether	a	certain	hypothesis	is	likely	to	be	true. For	our	purpose

>Whenever	a	random	variable	follows	a	normal	distribution,	we	can	use	normal_cdf	to figure	out	the	probability	that	its	realized	value	lies	within	(or	outside)	a	particular interval
