class caesar:
	def encrypt(self, text, key):
		newText = ""
		key = key % 26
		for i in text:
			if i.isupper():
				ch = ( ( ord(i) % 65 + key ) % 26 ) + 65
			else:
				ch = ( ( ord(i) % 97 + key ) % 26 ) + 97
			newText += chr(ch)
		print(newText)

	def decrypt(self, text, key):
		self.encrypt(text,26-key)

if __name__=='__main__':
	pf = caesar()
	print("Original text : Vikraman\nKey : 3")
	print("Encrypted text", pf.encrypt("Vikraman",3))
	print("Decrypted text", pf.decrypt("Ylnudpdq",3),"\n")