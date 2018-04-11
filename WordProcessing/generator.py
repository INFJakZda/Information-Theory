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
    words = [w.rstrip() for w in words if (len(w) > 0 and w != '\n' and w != '\t')]    
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


def mean_word_len(words):
    sum_len = 0
    for ele in words:
        sum_len += len(ele)
    print()
    print("Średnia długość słowa: " + str(sum_len / len(words)) )

def getWordAfter(words, word):
    list_words = []
    len_word = len(word)
    tmp_list = []
    for i in range(0, len_word):
        tmp_list.append(words[i])
    for ele in range(len_word, len(words)):
        if(tmp_list == word):
            list_words.append(words[ele])
        tmp_list.pop(0)
        tmp_list.append(words[ele])
    return list_words

def markov_chain(words, level, length):
    #random first word choise
    outText = []
    outText.append(words[random.randint(0, len(words) - 1)])
    #outText.append("probability")
    print(outText[0] + " ", end='', flush=True)
    for i in range(0, length):
        #find list of words after last words in outText        
        word_list = getWordAfter(words, outText[-level:])
        
        #if in this level there is no words - level down
        tmp_level = level
        while( len(word_list) == 0 and tmp_level > 1):
            tmp_level -= 1
            word_list = getWordAfter(words, outText[-tmp_level:])
        
        #from found words choise one in weighted propability
        new_word = word_list[random.randint(0,len(word_list)-1)]
        outText.append(new_word)
        print(new_word + " ", end='', flush=True)
    mean_word_len(outText)
    
def chain_generator1(words, level):
    chain = {}
    for ele in words:
        chain[ele] = []
    for it in range(0, len(words) - 1):
        word = words[it]
        wordAfter = words[it + 1]
        chain[word].append(wordAfter)
    print(chain)
    
def chain_generator(words, level):
    chain = {}

    tmp_list = words[0:level]
    #prepare the chain to have lists of words
    for i in range(level, len(words)):
        chain[str(tmp_list)] = []
        tmp_list.append(words[i])
        tmp_list.pop(0)
    chain[str(tmp_list)] = []
         
    tmp_list = words[0:level]     
    #fill the chain with words
    for i in range(level, len(words)):
        chain[str(tmp_list)].append(words[i])
        tmp_list.append(words[i])
        tmp_list.pop(0)
    #for ele in chain:
        #print(ele, "\t", chain[ele])
    return chain
    
def markov_gen(words, level, length):
    print("preparing chain....")
    chain = chain_generator(words, level)
    outText = []
    outText.append(words[random.randint(0, len(words) - 1)])
    #outText.append("probability")
    print(outText[0] + " ", end='', flush=True)
    #fill outText with random first words 
    while(len(outText) < level):
        word_list = getWordAfter(words, outText)
        tmp_level = level
        while( len(word_list) == 0 and tmp_level > 1):
            tmp_level -= 1
            word_list = getWordAfter(words, outText[-tmp_level:])
        new_word = word_list[random.randint(0,len(word_list)-1)]
        outText.append(new_word)
        print(new_word + " ", end='', flush=True)
    #main loop
    for i in range(level, length):
        word_list = chain[str(outText[-level:])]
        new_word = word_list[random.randint(0,len(word_list)-1)]
        outText.append(new_word)
        print(new_word + " ", end='', flush=True)    
    mean_word_len(outText)
        
        
    
if __name__ == '__main__':
    print("reading file...")
    #text = read_file("text.txt")
    text = read_file("data/norm_wiki_sample.txt")
    words = text_normaliser(text)
    
    #zad1
    #counter, cnt_len = words_counter(words, 30000, 30)
       
    #zad2.1
    #rand_text = words_generator(words, 100)
    #print(rand_text)
    #zad2.2
    #words_propab_gen(counter, cnt_len, 100)   
    
    #zad3.1
    #markov_chain(words, 2, 2000)
    
    #zad3.2
    markov_gen(words, 3, 20000)
    
