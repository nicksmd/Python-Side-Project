from random import randint
import os

def createInput(filename, number):
    text_file = open(filename, "w")
    for i in range(number):
        text_file.write(str(randint(1, 10000000)) + "\n")
    text_file.close()

class ExternalSort(object):
    def __init__(self, filename, ram):
        self.ram = ram
        self.filename = filename
        self.numberOfPart = (os.stat(filename).st_size / ram)+1
        self.partFiles = []

    def split(self):
        inputFile = open(self.filename, "r")
        count = 0
        while True:
            lines = inputFile.readlines(self.ram)
            if not lines:
                break

            lines = list(map(lambda x: x[:-1], lines))
            lines.sort()
            count+=1
            partFileName = "part_"+str(count) + ".txt"
            partFile = open(partFileName,"w")
            partFile.write(" ".join(lines))
            partFile.close()
            self.partFiles.append(partFileName)

    def merge(self):
        pass


if __name__ == "__main__":
    inputFile = "input.txt"
    outputFile = "output.txt"
    # byte
    ram = 1024*1024*2

    sorter = ExternalSort(inputFile, ram)
    sorter.split()




