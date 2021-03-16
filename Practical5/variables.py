a=200502
b=190784
c=100321
d=100181
e=90463
if d>e:
       	print("d>e")
else:
     	print("d<=e")

X=True
Y=False
Z=(X and not Y) or (Y and not X)
print(Z)
if Z==True:
	print("X or Y are ture.")
else:
     	print("X or Y are false.")

W = X!=Y
if W == Z:
	print("W and Z are always the same.")
else:
     	 print("W and Z are not the same.")
