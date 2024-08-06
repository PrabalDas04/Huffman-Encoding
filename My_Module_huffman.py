#####################################
'''
My Module containing all the definitions of the function used in Huffman_Encoding.py
'''
#####################################

class node:         # Huffman tree nodes containing it's symbol, ferquency and children information
    def __init__(self, freq, symbol, left = None, right = None): 
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.path = ''

class SourceNode:           # This is the final nodes conating source code and corresponding encoding 
    def __init__(self, symbol, code = '', prob = 0):
        self.symbol = symbol
        self.code = code
        self.prob = prob

# This function creates all the leaf nodes taking input from input file, each nodes are distinct. All are stored in
# a list named "List"
def CreateList(file): 
    c = file.read(1)
    New_Node = node(1,c,None,None)
    List = []
    List.append(New_Node)
    while 1:
        tag = 1
        c = file.read(1)
        c = c.lower()          # making all input character lower case
        # print(c)
        for v in List:
            if v.symbol == c:
                v.freq = v.freq + 1
                tag = 0
                break
        if(tag == 1):
            New_Node = node(1,c,None,None)
            List.append(New_Node)
        if c == '':         # when we encounter null character, we stop taking input
            break
    return List

# Function for selection sort
def SelectionSort(array, size):
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j].freq < array[min_index].freq:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array

# This function takes list of leaf nodes and creates the Huffman tree
def HuffmanTree(List):
    length = len(List)
    while(length > 1):
        sum_freq = List[0].freq + List[1].freq          # least two freq values are summed up
        conc_symbol = List[0].symbol + List[1].symbol   # those two symbol values are concatenated
        List[0].path = 0                                # edge weight
        List[1].path = 1
        New_Node = node(sum_freq,conc_symbol,List[0],List[1])
        List.pop(0)
        List.pop(0)
        List.append(New_Node)
        length = length - 1
        List = SelectionSort(List,length)
    return List[0]

List_source = []                   # Globally defined list for storing final source code and corresponding codes 

# function for assigning the code of each nodes of the Huffman tree
#after executing this funtion we will get a list of nodes with source symbol, code and prob = 0
def PrintCodes(Node, path):
    Newpath = path + str(Node.path)
    if(Node.left != None):
        PrintCodes(Node.left, Newpath)
    if(Node.right != None):
        PrintCodes(Node.right, Newpath)
    if(Node.right == None and Node.left == None):  # whenever we reach to a leaf node we appending that to the global list
        New_Node = SourceNode(Node.symbol,Newpath,0)
        List_source.append(New_Node)
        # print("Source symbol:",Node.symbol,", Code: ",Newpath)

# this function calculate the prob of occurence of each of the source code
# and calculate the expected code length 
def ExpCodeLength(List_buf, List_source, total):
    for v in List_buf:
        for u in List_source:
            if(v.symbol == u.symbol):
                u.prob = float(v.freq/total)
    PrintSourceNode(List_source)
    exp_code_length = 0
    for v in List_source:
        exp_code_length = exp_code_length + v.prob * len(v.code)
    print("Expected code length = ",exp_code_length)


# function for printing the final list ( the global list)
def PrintSourceNode(list):
    for v in list:
        print("Source symbol:",v.symbol,", Code: ",v.code,", length : ",len(v.code),"Prob : ",v.prob)

# function for printing the nodes
def PrintNodes(list):
    for v in list:
        print("symbol ",v.symbol," freq ",v.freq," left ",v.left.symbol," right ",v.right.symbol," path ",v.path)

# function prints the encoding of the input file and returns a output file
def PrintOutputFile(file):
    file1 = open("Huffman_output.txt","a")
    while(1):
        c = file.read(1)
        c = c.lower()
        for v in List_source:
            if(v.symbol == c):
                file1.write(v.code)
        if(c == ""):
            break
    file1.close()
    return file1

