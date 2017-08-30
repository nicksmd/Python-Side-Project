import time
import itertools

start_time = time.time()
number_of_step = 100000000

for i in itertools.count():
    if i> number_of_step : break

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
i = 0
while i <= number_of_step:
    i+=1

print("--- %s seconds ---" % (time.time() - start_time))