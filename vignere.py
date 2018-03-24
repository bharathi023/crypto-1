name=raw_input()
key=raw_input()
l=len(key)
c=[]
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(name)):
	m=i%l
	if key[m].isupper():
			k=A.find(key[m])
			if name[i].isupper():
				z=A.find(name[i])
				j=(z+k+1)%26
				c.append(A[j])
			elif name[i].islower():
				z=a.find(name[i])
				j=(z+k+1)%26
				c.append(a[j])
	else:
			k=a.find(key[m])	
			if name[i].isupper():
				z=A.find(name[i])
				j=(z+k+1)%26
				c.append(A[j])
			elif name[i].islower():
				z=a.find(name[i])
				j=(z+k+1)%26
				c.append(a[j])

print "".join(c)
