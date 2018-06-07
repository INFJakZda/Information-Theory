from heapq import heappush, heappop, heapify
from collections import Counter

data_file = "data/norm_wiki_sample.txt"

def heapsort(heap):
    heap_list = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return heapify(heap_list)

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq]
    #print(heap)
    heapify(heap)
    #print(heap)
#    for ele in heap:
#        print(ele)
    while len(heap) > 1:
        lo = heappop(heap)
        #print(lo)
        hi = heappop(heap)
        #print(hi)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        #heap = heapsort(heap)
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

f = open(data_file, "r")
txt = f.read()
#txt = "0123456789 abcdefghijklmnopqrstuvwxyz  albert of prussia 17 may 1490 20 march 1568 was the last grand master of the teutonic knights who after converting to lutheranism became the first monarch of the duchy of prussia the secularized state that emerged from the former monastic state of the teutonic knights albert was the first european ruler to establish protestantism as the official state religion of his lands he proved instrumental in the political spread of protestantism in its early stage ruling the prussian lands for nearly six decades 15101568 a member of the brandenburg ansbach branch of the house of hohenzollern albert s election as grand master had brought about hopes of a reversal of the declining fortune of the teutonic knights he was a skilled political administrator and leader and did indeed reverse the decline of the teutonic order however albert who was sympathetic to the demands of martin luther rebelled against the catholic church and the holy roman empire by converting the teutonic state into a protestant and hereditary realm the his uncle the king of"
#txt = "bbbetraaaa"

symb2freq = Counter(txt)
huff = encode(symb2freq.most_common())
print(huff)
print ("Symbol\tWeight\tHuffman Code")
for p in huff:
    print ("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))
