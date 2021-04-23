import csv
import pandas
user_import = input('Enter employee name: ')

#Funtion to find row number of employee
def find_index(input):
    record = open('hrdata_modified.csv', 'r')
    myData = csv.reader(record)
    index = 0
    for row in myData:
        #print (row)
        if (row)
         return index
         else : index+=1
val = find_index(user_input)
print (val)
if val is None:
    print ('Employee record not found!')
else:
    print('Employee record found.')
    newID = inpput('Enter new ID# (xx-xxx-xxxx'):')

reader = csv.reader(open('hrdata_modified.csv'))
lines = list(reader)



lines[val][4] = newID

w = open('output.csv', 'w', newLine='')
writer = csv.writer(w)
writer.writerows(lines)
w.close()

df = pandas.read_csv('output.csv')
    index_col='Employee'
    parse_dates=['Hired'],
    header=0
    names=['Employee', 'Hired', 'Salary, Sick Days', 'ID#'  ])

prind(df)

commit = input('Would you like to commit the changes? (Y/N)')

if commit == 'Y' or commit == 'y'
    df.to_csv('hrdata_modified.csv')
    print('Changes commited.')
else:
    print('Changes not commited.')
