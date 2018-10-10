import re
def remove_space(text):
		text = re.sub(" ","",text)
		return text
def format_text(text):
	text = text.upper()
	text = remove_space(text)
	return text
def encrypt(text,key):	
	text = format_text(text)
	cipher_text=""
	l=[]
	for i in range(0,key):
		l.append( [0]*len(text) )
	i=0
	j=0
	v=1
	for c in text:
		l[i][j]=c
		i+=v
		j+=1
		if i >= key:
			i-=2
			v=-1
		elif i <0:
			i+=2
			v=1
	for i in range(0,key):
		for j in range(0,len(text)):
			if l[i][j]!=0:
				cipher_text+=l[i][j]
	for i in l:
		print(i)
	return cipher_text
def decrypt(cipher,key):
	cipher = format_text(cipher)
	l=[]
	for i in range(0,key):
		l.append( [0]*len(cipher) )
	k=0
	text=""
	i=0
	j=0
	v=1
	for c in cipher:
		l[i][j]=1
		i+=v
		j+=1
		if i >= key:
			i-=2
			v=-1
		elif i <0:
			i+=2
			v=1
	k=0
	for i in range(0,key):
		for j in range(0,len(cipher)):
			if l[i][j] == 1:
				l[i][j] = cipher[k]
				k+=1 
	i=0
	j=0
	v=1
	for c in cipher:
		text+=l[i][j]
		i+=v
		j+=1
		if i >= key:
			i-=2
			v=-1
		elif i <0:
			i+=2
			v=1
	return text		
if __name__ == "__main__":
	text = "Vikraman sathiyanarayanan"
	key = 3
	print("Text  : " + text)
	print("Key : ",key)
	cipher = encrypt(text,key)
	print("Cipher: " + cipher)
	print("Decrpyt:" + decrypt(cipher,key))