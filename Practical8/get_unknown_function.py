import re
import os

os.chdir('/Users/A.BC.Perroquet/PycharmProjects/Practical8/venv')  # to change the working directory to where the fa file located in
seq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')    # to open the fa file
fl1 = seq.read()
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

gene = ""  # create an empty string for result
for i in range(len(name1)):
    gene += '>' + name1[i] + '       ' + str(len(series1[i])) + "\n" + series1[i] + "\n"  # a format for output

with open('unknown_function.fa', 'w') as output:    # creat a new .fa file
    unknown_function = open('unknown_function.fa', "w")
    unknown_function.write(gene)   # write results in
fin = open('unknown_function.fa', 'r')
print(fin.read())
unknown_function.close()
