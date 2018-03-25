import random
import numpy
import collections

def read_file(filename):
    f = open(filename, "r")
    return f.read()

def text_normaliser(text):
    #seperate words
    words = text.split(" ")    
    #delete whitespace , new line, tabs
    words = [w for w in words if (len(w) > 0 and w != '\n' and w != '\t')]    
    return words


def words_counter(words, noMostPop, noToPrint):
    most_popular = 0
    all_words = len(words)
    counter = collections.Counter(words)
    #print ascending
    for word in counter.most_common(noMostPop):
        if(noToPrint > 0):
            print(word, word[1] / all_words)
            noToPrint -= 1
        most_popular += word[1]
    #print(most_popular)
    #print(all_words)
    #print(most_popular / all_words)
    return counter, all_words
             
    #print random order    
    #for word in counter:
    #    print(word, counter[word])
    

#random words generator***********************
def words_generator(text, length):
    rand_text = ""
    len_text = len(text) - 1
    for i in range(length):
	    rand_text += text[random.randint(0, len_text)] + ' '
    return rand_text


#probability words generator*******************
def counter_normalise(counter, cnt_len):
    words = []
    prop_list = []
    for word in counter:
        words.append(word)
        prop_list.append(counter[word] / cnt_len)
    return words, prop_list     

def words_propab_gen(counter, cnt_len, length):
    words, prop_list = counter_normalise(counter, cnt_len)
    gen_words = ''
    for ele in range(length):
        gen_words += numpy.random.choice(words, p = prop_list) + " "
    #print(' '.join(gen_words))
    print(gen_words)


def getWordAfter(words, word):
    list_words = []
    len_word = len(word)
    tmp_list = []
    for i in range(0, len_word):
        tmp_list.append(words[i])
    for ele in range(len_word, len(words)):
        if(tmp_list == word):
            list_words.append(words[ele].rstrip())
        tmp_list.pop(0)
        tmp_list.append(words[ele])
    return list_words
        


def markov_chain(words, level, length):
    outText = []
    outText.append(words[random.randint(0, len(words) - 1)])
    for i in range(0, length):
        #print(outText)
        word_list = getWordAfter(words, outText[-level:])
        tmp_level = level
        while( len(word_list) == 0 and tmp_level > 1):
            print("ni ma szukamy: " + str(tmp_level))
            tmp_level -= 1
            word_list = getWordAfter(words, outText[-tmp_level:])
        outText.append(word_list[random.randint(0,len(word_list)-1)])
    print(outText)
    
    
if __name__ == '__main__':
    text = read_file("data/norm_wiki_sample.txt")
    #text = read_file("text.txt")
    words = text_normaliser(text)
    
    #zad1
    #counter, cnt_len = words_counter(words, 30000, 30)
       
    #zad2.1
    #rand_text = words_generator(words, 100)
    #print(rand_text)
    #zad2.2
    #words_propab_gen(counter, cnt_len, 100)   
    
    #zad3.1
    markov_chain(words, 2, 10)
    
