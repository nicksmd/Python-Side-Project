* itertool.count()

Looping with **for i in itertools.count()** is *measurable* faster than:

```python
i = 0
while True:
    ... do sth ...
    i+=1
```

Experiment:
```python
import time
import itertools

start_time = time.time()
number_of_step = 100000000
x = 0
for i in itertools.count():
    if i> number_of_step : break
    x+=1
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
i = 0
while i <= number_of_step:
    i+=1

print("--- %s seconds ---" % (time.time() - start_time))
```

result:
```python
--- 4.77500009537 seconds ---
--- 6.54299998283 seconds ---
```
*