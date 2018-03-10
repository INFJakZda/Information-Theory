import random
import numpy

dictionary = "abcdefghijklmnoprstuwxyz "
length = 10000000

def generator(string): 
    text = ""
    for x in range(0, length):
        index = random.randrange(len(string))
        text += dictionary[index]
    print(text)
    return text

def mean_length(string):
    i = 0
    length = 0
    listLength = []
    for lett in string:
        if lett == ' ':
            if length != 0:
                listLength.append(length)
            #print(length)
            length = 0
        else:
            length += 1
    print("Średnia")
    print(numpy.mean(listLength))

if __name__ == '__main__':
    string = generator(dictionary)
    mean_length(string)
    
