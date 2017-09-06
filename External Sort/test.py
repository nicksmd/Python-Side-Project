import itertools
import sys
x = [1,2,3,4,5]
y = iter(x)

file_object = open('part_1.txt','rb')
print sys.getsizeof(file_object)

# while True:
#     a =  file_object.readline()
#     if not a:
#         break
#     print a
#     print '-'


# for i in itertools.count():
#     chunk = file_object.readlines(5)
#     if not chunk:
#         break
#     print chunk
#     print "--"


# for a in list(itertools.islice(gengen(),10)):
#     print a