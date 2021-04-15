import csv

with open('NewCSV.csv', mode='w', newline='') as employee_file:
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['Name', 'Dept', 'Birth-month'])
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])