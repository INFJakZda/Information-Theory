import random
import numpy
import collections


def text_normaliser(text):
    #seperate words
    words = text.split(" ")    
    #delete whitespace , new line, tabs
    words = [w for w in words if (len(w) > 0 and w != '\n' and w != '\t')]    
    return words

def words_counter(words):    
    counter = collections.Counter(words)
    #print ascending
    for word in counter.most_common(100):
        print(word)     
    #print random order    
    #for word in counter:
    #    print(word, counter[word])

#random words generator
def words_generator(text, length):
    rand_text = ""
    len_text = len(text) - 1
    for i in range(length):
	    rand_text += text[random.randint(0, len_text)] + ' '
    return rand_text

def read_file(filename):
    f = open(filename, "r")
    return f.read()

if __name__ == '__main__':
    text = read_file("data/norm_wiki_sample.txt")
    words = text_normaliser(text)
    
    #zad1
    #words_counter(words)
       
    #zad2
    rand_text = words_generator(words, 100)
    print(rand_text)
    
    #zad3
    
