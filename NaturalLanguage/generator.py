import random
import numpy
import collections
import re

dictionary = "abcdefghijklmnoprstuwxyz 0123456789"
length = 100000

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
    
def conditional_generator(text):
    lett1, lett2 = collections.Counter(text).most_common(2)
    #detuple lett1 & lett2
    lett1, x = lett1
    lett2, x = lett2
    
    for w in [lett1, lett2]:
        text_len = len(text)
        lett_list = []      #list with letters after the most common
        
        for pos, char in enumerate(text):
            if(char == w and pos + 1 < text_len):
                lett_list.append(text[pos + 1])
                
        counter = collections.Counter(lett_list)
        total = sum(counter.values(), 0.0)
        #counter = {k: v / total for k, v in counter.items()}
        print("DLA " + w + " ******************")
        for word, freq in counter.most_common():
            print(word + "\t" + str(freq / total)) 


def getCharsAfter(text, lastChars):
    list_after_chars = []
    for ele in re.finditer(lastChars, text):
        if (ele.end() + 1 < len(text)):
            list_after_chars.append(text[ele.end()])
    return list_after_chars
    

def markov_chain(text, level, length):
    outText = ""
    if(level == 5):
        outText = "probability"
    else:
        baseWords = text.split()
        baseWords = [w for w in baseWords if (len(w) > 0 and w != '\n' and w != '\t')]
        outText = random.choice(baseWords)[:level]
    
    print(outText + ' ', end='', flush=True)
    for i in range(length):
        lastChars = outText[-level:]
        lett_list = getCharsAfter(text, lastChars)
        tmpLength = length
        while( len(lett_list) == 0):
            tmpLength -= 1
            lastChars = outText[-tmpLength:]
            lett_list = getCharsAfter(text, lastChars)
        newChar = lett_list[random.randint(0,len(lett_list)-1)]
        outText += newChar
        print(newChar, end='', flush=True)
    return outText

if __name__ == '__main__':
    print("reading file...")
    f = open("data/norm_wiki_sample.txt","r")
    string = f.read()
    #zad1
    #string = generator(dictionary, length)
    
    #zad2
    #mean_length(string)
    
    #zad3
    #prob_list = lett_counter(string, dictionary)
    #string = propability_generator(dictionary, prob_list)
    #mean_length(string)
    
    #zad4
    #conditional_generator(string)
    
    #zad5
    text = markov_chain(string, 5, 2000)
    #print(text)
