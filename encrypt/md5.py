def to_bin(val):
  b = bin(val)
  b = b[2:len(b)-2]
  return b
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
	i = 0
	x=[]
	while i < len(l):
		x.append(l[i:i+32])
		i+=32
	return l
def hexa(val):
	h = hex(val)
	return h[2:len(h)-2]
def f1(x,y,z):
	return (x & y) | (~x & z)
def f2(x,y,z):
	return (x & z) | (y & ~z)
def f3(x,y,z):
	return x^y^z
def f4(x,y,z):
	return y ^ (x | ~z)
def md5(text):
	l = padding(text)
	a = 2**10+100
	b  = 2**9+89
	c = 2**4+3789
	d = 2**10+900
	f = (f1,f2,f3,f4)
	hash_value = ""
	words=[]
	i = 0
	while i < len(l):
		words.append(l[i:i+512])
		i+=512
	hl = []
	for word in words:
		k = 0
		i =0
		x=[]
		while i < len(word):
			sl = word[i:i+8]
			s=""
			for ch in sl:
				s+=str(ch)
			x.append(int(s,2))
			i+=8
		for i in range(4):
			fun = f[i]
			for j in range(16):
				val = fun(b,c,d)
				a = b + a + val+x[k]
				a = a%2**32	
				t = a
				a = b
				b = c
				c = d
				d = t
				k+=1
	s = hexa(a)+hexa(b)+hexa(c)+hexa(d)
	return s
if __name__=="__main__":
	text = "Vikraman sathiyanarayanan is a good boy"
	hash_text =md5(text)
	print("Text is :",text)
	print ("Hased text : ",hash_text)