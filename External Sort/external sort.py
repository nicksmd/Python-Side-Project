from random import randint
import os
import heapq
import psutil

def createInput(filename, number):
    text_file = open(filename, "w")
    for i in range(number):
        text_file.write(str(randint(1, 10000000)) + "\n")
    text_file.close()

class ExternalSort(object):
    def __init__(self, filename, ram):
        self.ram = ram
        self.filename = filename
        self.numberOfPart = 0
        self.partFiles = []

    def split(self):
        inputFile = open(self.filename, "r")
        count = 0
        while True:
            lines = inputFile.readlines(self.ram)
            if not lines:
                break

            lines = list(map(lambda x: x[:-1], lines))
            lines = list(map(lambda x: int(x), lines))
            lines.sort()
            count+=1
            partFileName = "part_"+str(count) + ".txt"
            partFile = open(partFileName,"w")

            lines = list(map(lambda x: str(x), lines))

            partFile.write("\n".join(lines))
            partFile.close()
            self.partFiles.append(partFileName)

        self.numberOfPart = count

    def merge(self):
        first_elements = []
        for i in range(self.numberOfPart):
            file_obj = open(self.partFiles[i],'r')
            first_elements.append((int(file_obj.readline()), file_obj))

        outfile = open("output.txt", 'w')

        heap = []

        for e, file_obj in first_elements:
            heap.append((e,file_obj))

        heapq.heapify(heap)
        while heap:
            currentValue, file_obj = heap[0]
            outfile.write(str(currentValue)+"\n")

            first_element = file_obj.readline()
            if first_element:
                heapq.heapreplace(heap, (int(first_element), file_obj))
            else:
                heapq.heappop(heap)
                file_obj.close()

        outfile.close()

if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    # http://fa.bianp.net/blog/2013/different-ways-to-get-memory-consumption-or-lessons-learned-from-memory_profiler/
    inputFile = "input.txt"
    outputFile = "output.txt"
    # byte
    ram = 1024*1024*1 # 1MB

    sorter = ExternalSort(inputFile, ram)
    sorter.split()
    sorter.merge()

    print(process.memory_info().rss/1./1024/1024)