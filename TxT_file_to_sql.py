import re
import pyodbc

conn = pyodbc.connect('Driver={Sql Server};'
                      'Server=Rahul-Chouhan;'
                      'Database=Bulksms;'
                      'UID=sa;'
                      'Pwd=F21T21r5fcc;'
                      'Trusted_Connection=No;')


cursor = conn.cursor()


#Read the content of the text file

with open('R:\python_projects\warmup.txt', 'r') as file:
    file_content = file.read()

# Extract all "wcnt" values using regular expressions
matches = re.findall(r'"wcnt":(\d+)', file_content)

if matches:
    # print("wcnt values:")
    # for wcnt in matches:
#     #     print(wcnt)
# else:
#     print("No wcnt values found in the text file.")

 values = [int(wcnt) for wcnt in matches]
 Total_sum = sum(values)
 
sql = "Insert into MNPwarmupcount (Batch,Wcntcount,Date_of_batch) Values (8,?,'2023-05-26')"

try:
    cursor.execute(sql, Total_sum)
    cursor.commit()

except Exception as e:
    cursor.rollback()
    print("Error occre:", str(e))

else:
   print("Record Successfully Inserted")


cursor.close()
conn.close()
