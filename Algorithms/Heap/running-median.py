# https://www.hackerrank.com/challenges/find-the-running-median
"""
Algorithm: maintain a max heap that contains n/2+1 smallest elements, with n = number of element at current input stream

"""

import heapq
a = []
n = int(raw_input())
heap = []

replace_element = []

for i in range(n):
    #print replace_element
    x = -int(raw_input())
    count = (i+1)/2+1
    if len(heap) < count:
        heapq.heappush(replace_element, -x)
        pick = heapq.heappop(replace_element)
        heapq.heappush(heap, -pick)
    else:
        root = -heap[0]
        if -x < root:
            heapq.heapreplace(heap, x)
            heapq.heappush(replace_element, root)
        else:
            heapq.heappush(replace_element, -x)

    if i%2 ==0:
        print "%.1f"%((heap[0]+heap[0])*-1.0/2)
    else:
        print "%.1f"%((heap[0] + min(heap[1], heap[min(2, len(heap)-1)])) * -1.0 / 2)