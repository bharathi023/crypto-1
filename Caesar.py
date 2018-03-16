name=raw_input()
key=int(input())
c=[]
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(name)):
	if name[i].isupper():
		z=A.find(name[i])
		j=(z+key)%26
		c.append(A[j])
	else: 
		z=a.find(name[i])
		j=(z+key)%26
		c.append(a[j])

print "".join(c)
