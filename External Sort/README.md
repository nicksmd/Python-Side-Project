#### External sorting
External sorting is a term for a class of sorting algorithms that can handle massive amounts of data. External sorting is required when the data being sorted do not fit into the main memory of a computing device (usually RAM) and instead they must reside in the slower external memory (usually a hard drive). External sorting typically uses a hybrid sort-merge strategy. In the sorting phase, chunks of data small enough to fit in main memory are read, sorted, and written out to a temporary file. In the merge phase, the sorted sub-files are combined into a single larger file.

###### Problem:
Sort large text files in a minimum amount of memory

###### Inputs:

input_file  : Name of input file. input.txt

output_file : Name of output file, output.txt

mem: amount of memory to use for sorting, default: 2M





