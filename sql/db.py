import MySQLdb
class dbHelper:
	def __init__(self):
		self.db=MySQLdb.connect("localhost","student","student","security")
		self.cursor=self.db.cursor()

	def __enter__(self):
		return self

	def __exit__(self,exc_type, exc_value, traceback):
		self.db.close()

	def getId(self,user,password):
		self.cursor.execute("select id from users where username='{}' and password='{}'".format(user,password))
		return self.cursor.fetchall()
