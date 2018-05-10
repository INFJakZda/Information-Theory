from bitarray import bitarray
from collections import Counter
import pickle
from bitstring import BitArray
import filecmp

data_file = "data/norm_wiki_sample.txt"
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
    letters = Counter(text)
    dictionary = {}
    binary_index = 0
    for lett in letters.most_common():
        bin_rep = "{0:b}".format(binary_index)
        while(len(bin_rep) < 6):
            bin_rep = '0' + bin_rep
        dictionary[lett[0]] = bin_rep
        binary_index += 1
    return(dictionary)

def encode(text):
    dictionary = create(text)
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
    for i in range (0, len(bit_arr) - 5, 6):
        byte = bit_arr[i:i+6]
        if(len(byte) == 6):
            decoded += dictionary[byte]
    return ''.join(decoded) 
    

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
        
