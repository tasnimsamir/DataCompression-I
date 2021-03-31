from MinVar_Huffman_Classes import *
#VLC
string = input("Enter the string to compute Huffman Code: ")
#length of string
str_length = len(string)
unique_symbols = sorted(list(set(string)))
print("Unique characters are: ",unique_symbols)
#length of unique characters
lenchar = len(unique_symbols)
freq=[]
prob=[]
entropy_dict = {}
for i in range(lenchar):
    freq.append(string.count(unique_symbols[i]))
    prob.append(freq[i] / str_length)
    entropy_dict[unique_symbols[i]] = prob[i]

print("Entropy Dict: ",entropy_dict)
VLC = MinVar_huaffman()
sort_dict_desc = dict(sorted(entropy_dict.items(), key=lambda x: x[1], reverse=True))
VLC_Codes = VLC.Code_dict(sort_dict_desc)

print("Output Dictionary of MinVar Extended huffman: ",VLC_Codes)
print('=========================================================================================================')
#saving results as csv file
# import csv
# with open("VLC huffman.csv",'w') as fp:
#     root = csv.writer(fp )
#     root.writerow(["Symbol" , "Code"])
#     root.writerows(VLC_Codes.items())