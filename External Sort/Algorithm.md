### External sort

######Problem: sort a big file that does not fit into your ram

###### Algorithm:

- split the big file into multiple small files whose size is fit into memory. let n be number of element in each small file, k be number of small file. 

- sort each of small file. $\mathbb{O}(k*nlogn)$

- merge small files using heap

  - init an empty min heap

  - add all first element of all small files into heap

  - repeat: $\mathbb{O}(k*n)$

    - get the minimum element of heap and store it to the output file.

    - replace the heap root with the next element the small file from which the element is extracted. If this file is empty, remove the root heap.

      ​