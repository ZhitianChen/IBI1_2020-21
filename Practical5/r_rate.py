n=84 #start with 84 people.
r=1.4 #each infected individual will on average infect 1.4 individuals.
g=1 #count the generations of infecting
for g in range (1,6): #generate for 5 times
	n=n*(r+1) #calculate the infected people
	g=g+1 #the generation has increased 1 time
print n #print out the final result
