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
* Read file
- don't place the call to open file inside try/finally statement:
```python
file_object = open('myfile.txt')
try:
    for line in file_object:
       ...
finally:
    file_object.close()
```
because if there is an error while opening the file, there will be no file_object to close

- read the file a little at a time: read 100 bytes at a time
```python
file_object = open('myfile.txt','rb')
try:
    for i in itertools.count():
        chunk = file_object.read(100)
        if not chunk:
            break
        do_sth_with(chunk)
finally:
    file_object.close()
```
- readlines vs readline

    - readlines: faster, it reads the whole file at once and then split to lines.
    - readline: read a line at a time, slower.
