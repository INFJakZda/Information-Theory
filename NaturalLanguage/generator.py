import random
import numpy
import collections

#generates random string (with length) from given alphabet (dictionary)
def generator(dictionary, length): 
    string = ""
    for x in range(0, length):
        index = random.randrange(len(string))
        string += dictionary[index]
    print(string)
    return string

#mean length of words in given text
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

#counts number of occurrences of every letter in given string
def lett_counter(string, dictionary):
    letters = collections.Counter(string)
    length = len(string)

    for lett in dictionary:
        print(lett, letters[lett] / length )
    

if __name__ == '__main__':
    dictionary = "abcdefghijklmnoprstuwxyz "
    length = 10000000
    f = open("data/norm_wiki_sample.txt","r")
    string = f.read()
    #string = generator(dictionary)
    #mean_length(string)
    lett_counter(string, dictionary)
