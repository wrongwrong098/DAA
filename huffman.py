import heapq

class Node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left = self.right = None 
    
    def __lt__(self,other):
        return self.freq < other.freq
    
def print_codes(node,code=''):
    if node:
        if node.char:
            print(node.char,':',code)

        print_codes(node.left,code+'0')
        print_codes(node.right,code+'1')

def huffman(chars,freqs):
    steps=0
    heap = [Node(c,f)for c,f in zip(chars,freqs)]
    heapq.heapify(heap)
    steps+=len(heap)

    while len(heap) > 1 :
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
        steps+=1
        new = Node(None,l.freq + r.freq)
        new.left , new.right = l, r
        heapq.heappush(heap,new)


    print('Steps - ',steps)
    print('Huffman Codes !!')
    print_codes(heap[0])

chars = ['A','B','C','D','E']
freqs = [5,9,12,13,16]

huffman(chars,freqs)
