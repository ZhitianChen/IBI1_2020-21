import re
import os

os.chdir('/Users/A.BC.Perroquet/PycharmProjects/Practical8/venv')
# to change the working directory to where the fa file located in
Dictionary = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', ' TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TAA': 'O', 'TAG': 'U', 'TGT': 'C', 'TGC': 'C', 'TGA': 'X', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Z', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'J', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': ' T', 'AAT': 'N', 'AAC': 'B', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'D', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
# to create a dictionary containing the codons

filname = input()
fil = open(filname)
fl1 = fil.read()
fl1 = fl1+">"  # to fit with the method I use

str1 = ""
name1 = []  # to define a list for names of the genes
series1 = []  # to define a list for sequences of the genes

letter = '>'  # to avoid synax error in the for loop
m = 0
for letter in fl1:  # when there is '>' in the text
    i = fl1.find('>')
    j = fl1.find('>', 1)  # find the text between two '>'
    if len(fl1) == 1:  # when it comes to the end of the file, break the loop
        break

    text = fl1[i:j - 1]  # extract the text between two '>'
    fl1 = fl1[j:]  # remove the text from fil1

    if re.findall(r'unknown', text):
        k = text.find("_")  # to find out the name
        str1 = text[:k]
        name1.append(str1)

        k = text.find("]")  # to find out the sequence
        str1 = text[k + 1:]
        series1.append(str1)

        series1[m] = re.sub('\s+', '', series1[m].strip())  # remove the blank and the enter from the sequence
        m = m + 1

protein = []  # create an empty list to store protein sequence
for i in range(len(name1)):
    series1[i] = 'ATGCGACTACGATCGAGGGCC'
    groups = re.findall(r'[A-Z]{3}', series1[i])
    result = ''
    for a in range(0, len(groups)):
        result = result + Dictionary[groups[a]]
    protein.append(result)
    print(protein)

pro = ""  # create an empty string for result
for i in range(len(name1)):
    pro += '>' + name1[i] + '       ' "\n" + protein[0] + "\n"  # a format for output


with open('unknown_function_of_protein.fa', 'w') as output:    # creat a new .fa file
    unknown_function_of_protein = open('unknown_function.fa', "w")
    unknown_function_of_protein.write(pro)   # write results in
fin = open('unknown_function_of_protein.fa', 'r')
print(fin.read())
unknown_function_of_protein.close()
