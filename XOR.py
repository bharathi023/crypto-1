import string	
s=raw_input()

for key in range (256):
	l=""
	for i in range(0,len(s),2) :
		l+=(chr((int(s[i:i+2],16))^key))
	for j in l:
		if (j in string.printable):
			c=1
		else:
			c=0
			break
	if c==1 :
		print "for key = ", key ,"the string is : ","".join(l)	

