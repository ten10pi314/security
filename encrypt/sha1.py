def to_bin(val):
  b = bin(val)
  b = b[2:len(b)-2]
  return b
def hexa(val):
	h = hex(val)
	return h[2:len(h)-2]
def get_bits(t):
  l = []
  for i in t:
    val = ord(i)
    b = to_bin(val)
    b = "0"*(8-len(b))+b
    for bit in b:
      l.append(bit)
  return l
def padding(text):
	l = get_bits(text)
	rem = len(l)%512
	pad = 448-rem
	t = [0]*(pad-1)
	t = [1]+t
	l +=t
	rem = len(get_bits(text))%(2**64)
	b = to_bin(rem)
	b = "0"*(64-len(b))+b
	for bit in b:
		l.append(bit)
	return l
def circularshift(n,b):
	s = bin(n)
	s = s[2:]
	b = b%len(s)
	s = s[b:len(s)]+s[0:b]
	return int(s,2)
def hexa(val):
	h = hex(val)
	return h[2:len(h)-2]
def f(x,y,z,i):
	if i<20:
		return (x & y) | (~y & z)
	elif i <40:
		return x^y^z
	elif  i<60:
		return (x&y)|(y&z)|(x&z)
	elif i<80:
		return x^y^z	
def k(i):
	s1 = 2**10+100
	s2  = 2**9+89
	s3 = 2**4+3789
	s4 = 2**10+900
	if i<20:
		return s1
	elif i <40:
		return s2
	elif  i<60:
		return s3
	elif i<80:
		return s4
def sha1(text):
	l = padding(text)
	h1 = 2**8+98
	h2 = 2**7+76
	h3 = 2**22+332
	h4 = 2**6+5
	h5 = 2**7+21
	words=[]
	i = 0
	while i < len(l):
		words.append(l[i:i+512])
		i+=512
	for word in words:
		w=[]
		i=0
		while i<len(word):
			s=""
			for c in word[i:i+32]:
				s+=str(c)
			w.append(int(s,2))
			i+=32
		for i in range(16,80):
			val = w[i-3]^w[i-8]^w[i-14]^w[i-16]
			val = circularshift(val,1)
			w.append(val)
		a=h1
		b=h2
		c=h3
		d=h4
		e=h5
		for t in range(0,80):
			temp = circularshift(a,5)+f(b,c,d,i)+w[i]+k(t)
			e = d
			d = c
			c = circularshift(b,30)
			b = a
			a = temp
		h1 = h1+a
		h2 = h2+b
		h3 = h3+c
		h4 = h4+d
		h5 = h5+e
	return hexa(h1)+hexa(h2)+hexa(h3)+hexa(h4)+hexa(h5)
if __name__=="__main__":
	text = "Vikraman sathiyanarayana is a good boy"
	hash_text =sha1(text)
	print("Text is :",text)
	print("Hashed text :",hash_text)