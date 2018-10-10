class playfair:
	def formKey(self, key):
		k = []
		di = {chr(i):False for i in range(ord('a'),ord('z')+1)}
		for t in key:
			if not di[t]:
				k.append(t)
				di[t] = True
		ch = ord('a')
		while len(k) != 25:
			if chr(ch) == 'q':
				ch += 1
				continue
			if not di[chr(ch)]:
				k.append(chr(ch))
				di[chr(ch)] = True
			ch += 1
		
		keys = [k[0:5],k[5:10],k[10:15],k[15:20],k[20:25]]
		return keys

	def formText(self, text):
		if len(text) % 2 == 1:
			text += 'z'
		te = []
		while len(text) != 0:
			te.append(text[:2])
			text = text[2:]
		return te
	def getIndex(self, key):
		di = {chr(i):[0,0] for i in range(ord('a'),ord('z')+1)}
		for i in range(5):
			for j in range(5):
				di[key[i][j]] = [i,j]
		return di
	def encryptUtil(self, newText, newKey):
		index = self.getIndex(newKey)
		cipher = ""
		for i in newText:
			a = i[0]
			b = i[1]
			indA = index[a]
			indB = index[b]
			if indA[0] == indB[0]:
				x = indA[0]
				yA = (indA[1] + 1) % 5
				yB = (indB[1] + 1) % 5
				cipher += newKey[x][yA]
				cipher += newKey[x][yB]
			elif indA[1] == indB[1]:
				y = indA[1]
				xA = (indA[0] + 1) % 5
				xB = (indB[0] + 1) % 5
				cipher += newKey[xA][y]
				cipher += newKey[xB][y]
			else:
				xA, yA = indA[0], indB[1]
				xB, yB = indB[0], indA[1]
				cipher += newKey[xA][yA]
				cipher += newKey[xB][yB]
		print(cipher)
	def decryptUtil(self, newText, newKey):
		index = self.getIndex(newKey)
		cipher = ""
		for i in newText:
			a = i[0]
			b = i[1]
			indA = index[a]
			indB = index[b]
			if indA[0] == indB[0]:
				x = indA[0]
				yA = (indA[1] - 1 + 5) % 5
				yB = (indB[1] - 1 + 5) % 5
				cipher += newKey[x][yA]
				cipher += newKey[x][yB]
			elif indA[1] == indB[1]:
				y = indA[1]
				xA = (indA[0] - 1 + 5) % 5
				xB = (indB[0] - 1 + 5) % 5
				cipher += newKey[xA][y]
				cipher += newKey[xB][y]
			else:
				xA, yA = indA[0], indB[1]
				xB, yB = indB[0], indA[1]
				cipher += newKey[xA][yA]
				cipher += newKey[xB][yB]
		print(cipher)
	def encrypt(self, text, key):
		key = key.lower()
		key = ''.join(key.split())
		text = text.lower()
		text = ''.join(text.split())
		newKey = self.formKey(key)
		newText = self.formText(text)
		cipher = self.encryptUtil(newText, newKey)
	def decrypt(self, text, key):
		key = key.lower()
		key = ''.join(key.split())
		text = text.lower()
		text = ''.join(text.split())
		newKey = self.formKey(key)
		newText = self.formText(text)
		decipher = self.decryptUtil(newText, newKey)
if __name__=='__main__':
	pf = playfair()
	print("Original text : vikraman\nKey : macbook")
	print("Encrypted text", pf.encrypt("Vikraman","macbook"))
	print("Decrypted text", pf.decrypt("whdpcaoi","macbook"),"\n")