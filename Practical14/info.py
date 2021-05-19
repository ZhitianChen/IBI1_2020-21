from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DOMTree = xml.dom.minidom.parse('/Users/A.BC.Perroquet/PycharmProjects/Practical14/venv/go_obo.xml')  # input the xml file
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')  # to get all with tag 'term'

dict = {}    #make a empty dictionary
c = []      #make a empty list
for term in terms:      #make a dictonary including all childNodes
    dict[term.getElementsByTagName("id")[0].firstChild.data]=[]
for term in terms:
    id = term.getElementsByTagName("id")
    is_as = term.getElementsByTagName("is_a")
    for is_a in is_as:
        dict[is_a.firstChild.data].append(id[0].firstChild.data)
def count1(i):
    for term in terms:
        if i in term.getElementsByTagName("defstr")[0].firstChild.data:  #judge if wo find associated information
            ids = term.getElementsByTagName("id")[0].firstChild.data
            if dict[ids] != []:
                c = dict[ids]
                num = count2(c)
    print('Number of childNodes of all %s-associated terms: %d' % (i, num))
    return num
def count2(c):
    for i in range(len(c)):
        if c[i] not in listc:
            listc.append(c[i])  #childNodes
            count2(dict[c[i]])  #grandchildNodes
    return len(listc)
listc = []

dna = count1( "DNA")  #num = 8651
rna = count1("RNA")   #num = 17082
protein = count1("protein")  #num = 34029
car = count1("carbohydrate")  #num = 34373

data = {"DNA": dna, "RNA": rna, "Protein": protein, "Carbohydrate": car}
values = np.array([i for i in data.values()])
keys = np.array([j for j in data.keys()])
plt.pie(values, labels=keys, autopct='%1.2f%%')
plt.title("4 macromolecules")
plt.show()

DNA = find('DNA')
RNA = find('RNA')
Protein = find('protein')
Carbohydrate = find('Carbohydrate')

print('ChildNodes:')
print('DNA-related: '+str(DNA))
print('RNA-related: '+str(RNA))
print('Protein-related: '+str(Protein))
print('Carbohydrate-related: '+str(Carbohydrate))

