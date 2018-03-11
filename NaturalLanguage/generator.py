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
    length = 0
    prop_list = []
    for lett in dictionary:
        length += letters[lett]
        temp = letters[lett]
        prop_list.append(temp)
        
    for i in range(0, len(prop_list)):
        prop_list[i] = prop_list[i] / length
    return prop_list

#generates random string from alphabet & letter_propability list
#The approximation of the first row
def propability_generator(dictionary, prop_list):
    string = ""
    diction = []
    for lett in dictionary:
        diction.append(lett)
    string = numpy.random.choice(diction, length, p = prop_list)
    print(''.join(string))
    return string
    

if __name__ == '__main__':
    dictionary = "abcdefghijklmnoprstuwxyz 0123456789"
    length = 100000
    f = open("data/norm_wiki_sample.txt","r")
    string = f.read()
    #string = generator(dictionary, length)
    #mean_length(string)
    prob_list = lett_counter(string, dictionary)
    string = propability_generator(dictionary, prob_list)
    mean_length(string)
    
