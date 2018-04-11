import random
import numpy
import collections
import math

def read_file(filename):
    f = open(filename, "r")
    return f.read()

def text_normaliser(text):
    #seperate words
    words = text.split(" ")    
    #delete whitespace , new line, tabs
    words = [w.rstrip() for w in words if (len(w) > 0 and w != '\n' and w != '\t')]    
    return words

def entropy(dictionary, prop_list):
    hSum = 0
    for prop in prop_list:
        hSum += prop * math.log2(prop)
    print(-hSum)
    
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
    
def lett_entropy(dictionary, prop_list):
    for i in range(0, len(dictionary)):
        print(dictionary[i], prop_list[i])
    entropy(dictionary, prop_list)
    print(sum(prop_list))
        
    
if __name__ == '__main__':
    print("reading file...")
    dictionary = "abcdefghijklmnoprstuwxyz 0123456789"
    #text = read_file("text.txt")
    text = read_file("data/norm_wiki_en.txt")
    #words = text_normaliser(text)
    
    #zad1
    prop_list = lett_counter(text, dictionary)
    lett_entropy(dictionary, prop_list)
