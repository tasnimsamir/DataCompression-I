import numpy as np
import math

the_string = 'baaabaacaaabaaaa'
#length of string
string_length = len(the_string)
unique = sorted(list(set(the_string)))
print("Unique characters are: ",unique)
#length of unique characters
lenchar = len(unique)

freq = np.zeros((1,lenchar))
prob = np.zeros((1,lenchar))

entropy_dict = {}
#finding the value of probability
for i in range(lenchar):
    freq[0,i] = the_string.count(unique[i])
    prob[0,i] = freq[0,i] / string_length
    entropy_dict[unique[i]] = (prob[0,i]) #letter: (frequency,probabiity)

# print("frequency of each character:" , freq)
# print("the probability of each character: ", prob)
print("the entropy dictionary is: ",entropy_dict)

#information entropy
def Entropy(len_char , prob_vector):
    H = 0
    for i in range(len_char):
        H = H + (-prob_vector[0,i] * math.log(prob_vector[0,i],2))
    return H
def Redundancy(prob_dict , codestring_dict, entropy):
    avglen = 0
    for symbol in prob_dict:
        avglen = avglen + prob_dict[symbol] * len(codestring_dict[symbol]) #average length = prob * code length
    redund = avglen - entropy
    return avglen,redund

entropy = Entropy(lenchar,prob)
print("information entropy is: ", entropy)
print('=========================================================================================================')
#___________________________________________________________________________________________________________________________
#extended huffman code
extended_symbols = []
extended_prob = []
extended_dict={}

for i in range(lenchar):
    for j in range(lenchar):
        extended_symbols.append(unique[i]+unique[j])
        extended_prob.append(prob[0,i]*prob[0,j])
        extended_dict[unique[i]+unique[j]] = prob[0,i]*prob[0,j]

# print("Extended symbols are: " , extended_symbols )
# print("Extended frequencies are: " , extended_prob)
print("Extended dictionary are: " , extended_dict)
from MinVar_Huffman_Classes import *

extended_huffman_minVar = MinVar_huaffman()
sort_dict_desc = dict(sorted(extended_dict.items(), key=lambda x: x[1], reverse=True))
ex_minVar_codes = extended_huffman_minVar.Code_dict(sort_dict_desc)

print("Output Dictionary of MinVar Extended huffman: ",ex_minVar_codes)
# print("Output reverse Dictionary: ",reverse_mapping)

avglength1,redundancy1 = Redundancy(extended_dict , ex_minVar_codes , entropy)

print("AvgLength of MinVar Extended huffman = {} \nRedundancy of MinVar Extended huffman = {}\n".format(avglength1,redundancy1))

encoded_text = extended_huffman_minVar.get_extended_encoded_text(the_string,string_length)
print("Encoded text of MinVar Extended huffman :",encoded_text)
print('=========================================================================================================')
# ________________________________________________________________________________________________________________
#Canonical hauffman code
MAX_CODE_BIT_LENGTH = 8
def Canonical_Huffman(minVar_codes):
    lengths_dict = {}
    canonical_dict={}
    minVar_codes = dict(sorted(minVar_codes.items(), key=lambda x: x[0], reverse=False)) #sort according to keys(for lexigraphical order)

    for symbol in minVar_codes:
        lengths_dict[symbol] = len(minVar_codes[symbol])
    lengths_dict = (sorted(lengths_dict.items(), key=lambda x: x[1], reverse=False))#sort according to values
    # get bit range
    minbits = lengths_dict[0][1]
    maxbits = lengths_dict[-1][1]
    # make sure our codes comply with the length constraints
    assert minbits > 0
    assert maxbits <= MAX_CODE_BIT_LENGTH
    # now we build the canonical codes, replacing the previously calculated codes as we go.
    code = 0
    canonical_dict[lengths_dict[0][0]] = str(code)
    numsymbols = len(lengths_dict)
    for n in range(1,numsymbols):
        k = lengths_dict[n]  # tuple (symbol, bitlength)
        bitlength = k[1]
        code = (code + 1)
        codestring = format(code,'b').ljust(bitlength,'0')  # convert the code to a binary format string, leading zeros set to bitlength
        code = int(codestring,2)
        canonical_dict[k[0]] = codestring
    return canonical_dict


canonical_dict = Canonical_Huffman(ex_minVar_codes)
print("Canonical Dictionary: ", canonical_dict)

avglength2,redundancy2 = Redundancy(extended_dict , canonical_dict , entropy)

print("AvgLength of Canonical MinVar Extended huffman = {} \nRedundancy of Canonical MinVar Extended huffman = {}".format(avglength2,redundancy2))
print('=========================================================================================================')
#____________________________________________________________________________________________________________________________________
#Saving results as csv file
import csv

# with open("minVar Extended huffman output.csv",'w') as fp:
#     root = csv.writer(fp )
#     root.writerow(["Symbol" , "Code"])
#     root.writerows(ex_minVar_codes.items())
#     root.writerow(["Average length",avglength1])
#     root.writerow(["Redundancy" , redundancy1])
#
#
# with open("Canonical minVar Extended huffman output.csv",'w') as fp:
#     root = csv.writer(fp )
#     root.writerow(["Symbol" , "Code"])
#     root.writerows(canonical_dict.items())
#     root.writerow(["Average length",avglength2])
#     root.writerow(["Redundancy" , redundancy2])


# with open("Entropy.csv",'w') as fp:
#     root = csv.writer(fp )
#     root.writerow(["Symbol" , "Probability" ])
#     root.writerows(entropy_dict.items())
#     root.writerow(['Entropy' , entropy])