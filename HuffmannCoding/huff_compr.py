from bitarray import bitarray
from collections import Counter
import pickle
from bitstring import BitArray
from heapq import heappush, heappop, heapify
import filecmp

data_file = "data/norm_wiki_sample.txt"
#data_file = "data/test.txt"
file_code = "code.dat"
file_text = "decoded_text.txt"
dict_file = "dictionary"
zip_dir = "zip/"
unzip_dir = "unzip/"

#******************************************************* 

def save_obj(obj):
    with open(zip_dir + dict_file + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def create(text):
    letters = Counter(text).most_common()
    #create list of [weigth, [letter, code]]
    heap = [[wt, [sym, ""]] for sym, wt in letters]
    #create heap from list
    heapify(heap)
    #create tree from heap
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        #print(lo)
        #print(hi)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    list_code = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    dictionary = {}
    for ele in list_code:
        dictionary[ele[0]] = ele[1]
    return dictionary
    #print(dictionary)

def encode(text):
    dictionary = create(text)
    #print(dictionary)
    save_obj(dictionary)
    code = []
    for lett in text:
        code.append(dictionary[lett])
    return bitarray(''.join(code)).tobytes()

def save():
    print("[INFO] Read data")
    f = open(data_file, "r")
    text = f.read()
    print("[INFO] encoding")
    coded_text = encode(text)
    print("[INFO] Save zip code")
    w = open(zip_dir + file_code, "wb")
    w.write(coded_text)
    
#******************************************************* 

def load_obj():
    with open(zip_dir + dict_file + '.pkl', 'rb') as f:
        return pickle.load(f)
        
def decode(code):
    dictionary = load_obj()
    dictionary = {v: k for k, v in dictionary.items()}
    bit_arr = BitArray(bytes = code).bin
    decoded = []
    code = bit_arr[0]
    for i in range (1, len(bit_arr) - 3):
        if code in dictionary:
            decoded += dictionary[code]
            code = bit_arr[i]
        else:
            code += bit_arr[i] 
    return ''.join(decoded)
    #return out_text    

def load():
    print("[INFO] Read coded data")
    r = open(zip_dir + file_code, "rb")
    code = r.read()
    print("[INFO] decoding")
    decoded = decode(code)
    print("[INFO] Save decoded text")
    w = open(unzip_dir + file_text, 'w')
    w.write(decoded)

#******************************************************* 
    
if __name__ == '__main__':   
    save()
    load()
    print("[RESULT] " + str(filecmp.cmp(unzip_dir + file_text, data_file)))
    
    
'''
    text = read_file(data_file)
    print(text)
    for lett in text:
        asci = ord(lett)
        if(asci == 10):
            pass
        else:        
            if(asci < 58):
                asci -= 48
            if(asci > 95):
                asci -= 86
        byte = asci.to_bytes(1, byteorder = 'big', signed = True)
        binary = "{0:b}".format(asci)
        
        while(len(binary) < 6):
            binary = '0' + binary
        print(lett, asci, byte, binary, ord(binary))
'''
        
