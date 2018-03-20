import random
import numpy
import collections

def words_counter(text):
    #seperate words
    words = text.split(" ")
    
    #delete whitespace , new line, tabs
    words = [w for w in words if (len(w) > 0 and w != '\n' and w != '\t')]
    
    counter = collections.Counter(words)

    #print ascending
    for word in counter.most_common(100):
        print(word) 
    
    #print random order    
    #for word in counter:
    #    print(word, counter[word])

def read_file(filename):
    f = open(filename, "r")
    return f.read()

if __name__ == '__main__':
    
    text = read_file("data/norm_wiki_sample.txt")
    #zad1
    words_counter(text)
    
    #zad2
    
    #zad3
    
