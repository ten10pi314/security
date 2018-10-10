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
	key = format_text(key)
	cipher_text=""
	k=0
	for i in text:
		val1 = ord(i)-65
		val2 = ord(key[k])-65
		val = (val1+val2)%26
		c=chr(65+val)
		cipher_text+=c
		k=(k+1)%(len(key))	

	return cipher_text
def decrypt(cipher,key):
	cipher = format_text(cipher)
	key = format_text(key)
	text=""
	k=0
	for i in cipher:
		val1 = ord(i)-65
		val2 = ord(key[k])-65
		val = (val1-val2)%26
		c=chr(65+val)
		text+=c
		k=(k+1)%(len(key))	
	return text 
if __name__ == "__main__":
	text = "Vikraman"
	key = "mac"
	print("Text  : " + text)
	print("Key : "+key)
	cipher = encrypt(text,key)
	print("Cipher: " + cipher)
	print("Decrpyt:" + decrypt(cipher,key))