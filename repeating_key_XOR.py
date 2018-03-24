pt=raw_input()
key=raw_input()
l=len(key)
ct=[]
for i in range (0,len(pt)):
	j=i%l
	ct.append(hex(ord(pt[i])^ord(key[j]))[2:].zfill(2))
print "".join(ct)
