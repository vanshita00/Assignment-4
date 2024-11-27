# little change in that....Now, slight change, you have not to insert all filtered objects of WR and MH, you just 
# have to go through the JSON data like Rajat is doing for WR, so if he encounter first WR record then he dont need 
# to go further to json data, just create a record of WR on current date and return "Data inserted for WR" and if 
# he never encounter WR in whole json then just return Data Not found
# similar for Vanshita in case of MH
# and if that date record already exist for WR or MH respectively, then increase the revision no by 1 and inset 
# record


import mysql.connector
import json
from datetime import datetime

def get_data(source_name,revision_no):
        database=mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='vanshita1234@', 
            database='python_training'
        )
        with open('data_set_python_training.json','r') as file:
            data=json.load(file)
        
        for item in data:
            if item.get('source_name')==source_name:
                db=database.cursor()
                current_date=datetime.now().date()
                
       
                check="""SELECT revision_no FROM schedule_revision_details
                    WHERE source_name = %s AND DATE(entry_date) = %s"""
                db.execute(check,(source_name, current_date))
                result=db.fetchall()

                if result:
                    # print(result)

                    print(len(result))
                    temp=len(result)
                    revision_no=result[temp - 1][0] + 1

                    # revision_no = 55
                
               
             
              
                db=database.cursor()

            
                insert="""INSERT INTO schedule_revision_details
                  (source_name, entry_date, revision_no, created_at, updated_at)VALUES 
                  (%s, %s, %s, %s, %s)"""
                timestamp=datetime.now()
                db.execute(insert,(source_name,timestamp,revision_no,timestamp,timestamp))
               
                return f"Data inserted for {source_name}"
        
        return "Data not found"

result = get_data("MH", 1)
print(result)


