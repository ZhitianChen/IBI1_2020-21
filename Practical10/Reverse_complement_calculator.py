def dna(seq):  # define a new function
    seq = str(seq.upper())  # change the letters to uppercase
    seq_list = list(seq)  # let the string become a list
    rc_DNA = ''
    mylist = []  # create a new empty list
    for i in seq_list:  # change it to the complementary strand
        if i == 'A':
            mylist.append('T')
        elif i == 'T':
            mylist.append('A')
        elif i == 'C':
            mylist.append('G')
        elif i == 'G':
            mylist.append('C')
    rc_DNA = ''.join(mylist)
    rc_DNA = rc_DNA[::-1]
    print(rc_DNA)  # print the sequence
    return rc_DNA

seq = 'ATTGCGGGTACGTTTCTCGGGGT'  # the example for input
dna(seq)  # to call the function with the input of 'seq'
