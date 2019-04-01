import csv
import sys

def get_file():
  try:
    csv_file = sys.argv[1]
  except IndexError:
    csv_file = "import_me.csv"
    print("No file was given, working with default file: import_me.csv")

  return csv_file

def read_csv(csv_file="import_me.csv"):
  rows = []
  with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, dialect='excel')
    fields = csvreader.__next__()
        
    for row in csvreader: 
      rows.append(row)

    print(f'Total no. of rows: {csvreader.line_num}', flush=True) 
    print('Field names are: \n' + ', '.join(field for field in fields))
    print('\nHere is the Table:')

    for row in rows:
      for col in row: 
        print(f'{col}', end="   ")
      print("")

read_csv(get_file())