import sqlite3
 
db = sqlite3.connect("database.db") 
cursor = db.cursor()
 
cursor.execute("""CREATE TABLE tasks
                  (category text, description text, task_date text,
                   task_time text, status text)
               """)
