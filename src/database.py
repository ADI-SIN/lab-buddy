import sqlite3

conn = sqlite3.connect('video_db.db')
print("Opened database successfully");
try:
    conn.execute('CREATE TABLE videos (id INT, topic TEXT, url TEXT)')
    print("Table created successfully");
    conn.close()
except sqlite3.OperationalError as e:
    print("Error occurred while creating the table: "+str(e))

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('video_db.db')
        print("Opened database successfully");
        host = "127.0.0.1"
        user = "newuser"
        password = ""
        db = "training"
        self.cur = self.conn.cursor()

    def list_topic(self,topic):
    	sql="SELECT * FROM videos where topic = ?;"
    	val=(topic,)
    	self.cur.execute(sql,val)
    	result=self.cur.fetchall()
    	return result

    def store_student(self,roll,clas,fname,lname):

    	sql='CALL store_stud(%s,%s,%s,%s)'
    	val2=(roll,fname,lname,clas)
    	self.cur.execute(sql,val2)
    	self.conn.commit()
    	result = self.cur.fetchone()
    	return result

    def __del__(self): 
    	self.conn.close()

