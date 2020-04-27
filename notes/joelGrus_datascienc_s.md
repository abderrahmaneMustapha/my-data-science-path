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
