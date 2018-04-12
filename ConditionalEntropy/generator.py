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
        
#def lett_cond_entropy(level, text):
def chain_prepare(words, level):
    chain = {}
    tmp_list = words[0:level]
    for i in range(level, len(words)):
        chain[' '.join(tmp_list)] = {}
        tmp_list.append(words[i])
        tmp_list.pop(0)
    chain[' '.join(tmp_list)] = {}
    return chain

def ngram_list(text,n):  
    ngram=[]
    chain = chain_prepare(text, n)
    count = 0  
    for token in text[:len(text)-n+1]:  
        nkey = text[count:count+n]
        ngram.append(nkey)
        if(len(text) > count + n):
            chain[' '.join(nkey)][text[count+n]] = (chain[' '.join(nkey)][text[count+n]] + 1) if text[count+n] in chain[' '.join(nkey)] else 1
        count=count+1  
    return ngram, chain

def ngram_counts(text, n):
    ngram_d = {}
    ngram_l, chain = ngram_list(text, n)

    for item in ngram_l:
        ngram_d[' '.join(item)] = (ngram_d[' '.join(item)] + 1) if ' '.join(item) in ngram_d else 1 
    return ngram_d, chain

def condentropy(data, level):
    uni_gram, chain = ngram_counts(data, 1)
    n_gram, chain = ngram_counts(data, level)
    '''for key in n_gram:
        print(key + "\t" + str(n_gram[key]))
    for key in chain:
        print(key + "\t" + str(chain[key])) '''
    #return 0
    N = sum(uni_gram.values())
    H = 0
    #uni_gram[''] = 0.0
    #bi_gram[''] = 0.0   
    '''
    for key in uni_gram.keys():
        print(key, uni_gram[key])
    print("tera BI GRAM")
    for key in bi_gram.keys():
        print(key, bi_gram[key])
    '''
    for key in n_gram.keys():
        pr_con = 0
        sum_con = sum(chain[key].values())
        for con_val in chain[key].values():
            pr_tmp = (con_val / sum_con)
            pr_con += (pr_tmp * 1.0) * math.log2(1.0 / pr_tmp)        
        #H -= (n_gram[key] / (1.0 * N)) * (math.log2(bi_gram[key]  (1.0 * uni_gram[key.split(' ')[level-1]])))
        H += (n_gram[key] / (1.0 * N)) * pr_con 
    
    print(H)  

def word_cond_entropy(text):
    uni_gram, chain = ngram_counts(text, 1)
    N = sum(uni_gram.values())
    prop_list = [val / N for val in uni_gram.values()]
    entropy("", prop_list)
    
    
    
if __name__ == '__main__':
    print("reading file...")
    dictionary = "abcdefghijklmnoprstuwxyz 0123456789"
    #text = read_file("text.txt")
    text = read_file("data/sample0.txt")
    #words = text_normaliser(text)
    text = text_normaliser(text)
    
    #zad1
    #prop_list = lett_counter(text, dictionary)
    #lett_entropy(dictionary, prop_list)
    
    #zad2
    #2.1 - eng word DONE
    #word_cond_entropy(text)

    #2.2 - eng words DONE 
    #for level in range(1, 4):
    #    print("Doing level ", str(level + 1))
    #     condentropy(text, level)
    
    #2.1 - words universal from 0 to level
    print("Doing level " + "0")
    word_cond_entropy(text)
    for level in range(1, 5):
        print("Doing level ", str(level))
        condentropy(text, level)
    
    #2.3 - eng lett
    
    #2.4 - eng lettrs
    
        
