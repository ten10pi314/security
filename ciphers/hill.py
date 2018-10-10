import re
import random
import numpy as np
import math
def multiply(t,key):
	l=[]
	for i in range(0,len(t)):
		l.append([])
		l[i].append(ord(t[i])-65)
	a = np.matrix(key)
	b = np.matrix(l)
	c = a*b
	ct=""
	for i in c:
		ct += chr(65+(i%26))
	return ct
def encrypt(text,key):	
	cipher_text=""
	a = key
	b =[]
	i=0
	while i<len(text):
		cipher_text+=multiply(text[i:i+len(key)],key)
		i+=len(key)
	return cipher_text
def inv_det(d):
	for i in range(0,26):
		if (i*d)%26==1:			return i
def divide(t,key):
	l=[]
	for i in range(0,len(t)):
		l.append([])
		l[i].append(ord(t[i])-65)
	a = np.matrix(key)
	b = np.matrix(l)
	c = a*b
	c = c%26
	ct=""
	l=[]
	l=c.tolist()
	for i in range(len(l)):
		ch =  l[i]
		ch = round(ch[0],0)
		ch = int(ch)
		l[i]=ch%26
	for i in range(len(l)):
		ch = l[i]
		ct += chr(65+ch)
	return ct
def decrypt(cipher,key):
	k=np.matrix(key)
	d = int(np.linalg.det(k))
	inv=k.I
	for i in range(0,len(inv)):
		inv[i]*=d
		id = inv_det(d)
		inv[i]=(inv[i]*id)%26		

	text=""
	i=0	
	while i < len(cipher):
		text += divide(cipher[i:i+len(key)],inv)
		i+=len(key)
	return text	
def find_key_matrix(key):
	l = int(math.sqrt(len(key)))
	mat = []
	for i in range(0,len(key),l):
		li = []
		for j in range(0,l):
			li.append(ord(key[i+j])-ord('A'))
		mat.append(li)
	return mat

if __name__ == "__main__":
	text = "VIK"
	Key = "GYBNQKURP"
	key = find_key_matrix(Key)
	print("Text  : " + text)
	print("Key : ",key)
	cipher = encrypt(text,key)
	print("Cipher: " + cipher)
	print("Decrpyt:" + decrypt(cipher,key))