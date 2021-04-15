import csv

with open('testCS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',' quotechar='"', skipinitialspace=True)
    line_count = 0, csv.reader, (csv_file, skipinitialspace=True)
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}')
            line_count += 1
    print(f'Processed {line_count} lines.')