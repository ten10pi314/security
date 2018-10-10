import re
import random
import math
def remove_space(text):
		text = re.sub(" ","",text)
		return text
def format_text(text):
	text = text.upper()
	text = remove_space(text)
	return text
def is_prime(x):
    if x == 2:
        return True
    else:
        for number in range (3,x): 
            if x % number == 0 or x % 2 == 0:
         #print number
                return False
        return True
def get_prime(no):
	i = 2
	count = 1
	
	if no == 1:
		return i
	while True:
		if is_prime(i)==True:
			count+=1
		if count==no:
			return i
		i+=1
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def get_public_key1():
	p = get_prime(random.randint(1,50))
	q = get_prime(random.randint(1,50))
	return p*q
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
def get_public_key2(n):
	totient = phi(n)
	i =n-1
	while i >0:
		if gcd(i,totient)==1:
			return i
		i-=1
	raise "Co-prime not found exception"
def to_cipher(m,e,n):
	c = ord(m)-65
	v = c**e
	v = v%n
	return int(v)
def encrypt(text,key):
	text = format_text(text)
	e,n = key[0],key[1]
	cipher_text =[]
	for i in text:
		cipher_text.append(to_cipher(i,e,n))
	return cipher_text
def inv_mod(a,b):
	for i in range(1,b):
		if (a*i)%b == 1:
			return i
	raise "Imverse not found"

def find_d(e,n):
	totient = phi(n)
	return inv_mod(e,totient)
def to_normal_text(val,d,n):
	val = val**d
	val = val % n
	return chr(65+val)
def decrypt(cipher,key):
	text =""
	e,n = key[0],key[1]
	d = find_d(e,n)
	for i in cipher:
		val = i#ord(i)-65
		text += to_normal_text(val,d,n)
	return text
if __name__ == "__main__":
	text = "Vikraman sathiyanarayanan"
	n = get_public_key1()
	e = get_public_key2(n)
	key = (e,n)
	print("Text :",text)
	print("Key :",key)
	cipher = encrypt(text,key)
	print("Encrypted text :",cipher)
	print("Decrypted text :",decrypt(cipher,key))