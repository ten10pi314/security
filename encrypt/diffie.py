import math
import random
def is_prime(x):
    if x == 2:
        return True
    else:
        for number in range (3,x): 
            if x % number == 0 or x % 2 == 0:
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
def calculate_y(x,g,p):
	v = g**x
	return int(v % p)
def calculate_z(y,x,p):
	v =y**x
	return int(v%p)
def differ_hillman(p,g):
	Xa = random.randint(1,p)
	Xb = random.randint(1,p)
	Ya = calculate_y(Xa,g,p)
	Yb = calculate_y(Xb,g,p)
	Za = calculate_z(Yb,Xa,p)
	Zb = calculate_z(Ya,Xb,p)
	print("Prime nos :",p,g)
	print("Private and public key of A :",Xa,Ya)
	print("Private and public key of B :",Xb,Yb)
	if Za == Zb:
		print("Sucessful key_exchange between a and b")
	else:
		print("key_exchange failed")
if __name__== "__main__":
	p = get_prime(random.randint(1,100))
	g = random.randint(1,100)
	differ_hillman(p,g)