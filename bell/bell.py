users = {
	'restricted':[['abinav','12345'],['timothy','23456']],
	'confidential':[['akshay','34567'],['deepak','45678']],
	'secret':[['gowtham','567890']],
	'topsecret':[['vikraman','23456'],['kesavan','45678']]
}

files = {
	'restricted':['abc.txt'],
	'confidential':['def.txt'],
	'secret':['ghi.txt'],
	'topsecret':['jkl.txt']	
}

classification = {
	1: 'restricted',
	2: 'confidential',
	3: 'secret',
	4: 'topsecret'
}

def check(username, password):
	for i in range(1,5):
		cl = classification[i]
		for j in range(len(users[cl])):
			if username==users[cl][j][0] and password==users[cl][j][1]:
				return False
	return True

def getprivilege(username):
	for i in range(1,5):
		cl = classification[i]
		for j in range(len(users[cl])):
			if username==users[cl][j][0]:
				return cl

def printPossibleFiles(privilege,nu,li):
	num = 0
	for i in range(1,5):
		if classification[i]==privilege:
			num = i
	for i in range(num,li,nu):
		cl = classification[i]
		print(cl,end=' : ')
		for j in range(len(files[cl])):
			print(files[cl][j],end=' ')
		print()

while True:
	user = input('Enter username')
	pas = input('Enter password')
	while check(user,pas):
		user = input('Enter username')
		pas = input('Enter password')

	prev = getprivilege(user)

	while True:
		choice = input('Do you want to read/write?[r/w]')
		if choice=='r':
			printPossibleFiles(prev,-1,0)
		elif choice=='w':
			printPossibleFiles(prev,1,5)
		else:
			print('Wrong choice')
		log = input('Do you want to logout?[Y/n]')
		if log == 'Y':
			break
	x = input('Do you want to continue?[Y/n]')
	if x == 'n':
		break