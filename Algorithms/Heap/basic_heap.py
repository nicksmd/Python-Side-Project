import heapq
n = int(raw_input())
heap = []
for i in range(n):
    inp = raw_input().split()
    if len(inp) == 2:
        q,v = map(int, inp)
    else:
        q = int(inp[0])

    if q == 1:
        heapq.heappush(heap, v)
    else:
        if q == 2:
            if v == heap[0]:
                heap.remove(v)
                heapq.heapify(heap)
            else:
                heap.remove(v)
        else:
            print heap[0]