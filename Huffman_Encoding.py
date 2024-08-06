###########################################################################
'''
Programme for Huffman Encoding Scheme
Author : Prabal Das, CrS 2nd Sem, ISI
Date : 14.03.2024
'''
###########################################################################
import My_Module_huffman

# driver code
if __name__ == "__main__":
    file = open("Huffman_input.txt","r")    #input file
    List_Nodes = []
    List_Nodes = My_Module_huffman.CreateList(file)
    file.close()
    length = len(List_Nodes)
    List_Nodes = My_Module_huffman.SelectionSort(List_Nodes, length)
    List_Nodes_buf = []
    List_Nodes_buf = List_Nodes.copy()
    total = 0       # total no of character in the input file
    for v in List_Nodes_buf:
        total = total + v.freq
    root = My_Module_huffman.HuffmanTree(List_Nodes)
    My_Module_huffman.PrintCodes(root, root.path)
    My_Module_huffman.ExpCodeLength(List_Nodes_buf,My_Module_huffman.List_source,total)
## Till now we get a list of nodes(List_source) which contains all the source symbols, corr. code and prob of occcurence
    file = open("Huffman_input.txt","r")
    file1 = My_Module_huffman.PrintOutputFile(file)
    file.close()