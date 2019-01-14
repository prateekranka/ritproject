import csv
import sys

# if len(sys.argv) < 2:
#   print "Usage: ./csv-html.py <your CSV file> <your HTML File.html>"
#   print
#   print
#   exit(0)

# Open the CSV file for reading
# reader = csv.reader(open(sys.argv[1]))
datadict_path = 'C:\Users\USER\Downloads\RIT\Deliverables\\'
reader = csv.reader(open(datadict_path + 'Data Dictionary_Inv.csv'))

# Create the HTML file
f_html = open('Inventory.html',"w")
f_html.write('<title>Inventory Data Dictionary</title>')
f_html.write('<form>')
f_html.write('<table>')
for row in reader: # Read a single row from the CSV file
  # print "Reader"
  # print reader
  # print "Row"
  # print row
  f_html.write('<tr>')# Create a new row in the table
  for column in row: # For each column..
    # print "Column"
    # print column
    # if (column=='INPUT'):
    #   print "Inside IF"
    #   print column
    #   f_html.write('<td>' + '<INPUT TYPE="TEXT" NAME="name" SIZE="20">' + '</td>')
    # else:
    f_html.write('<td>' + column + '</td>')
    f_html.write('</tr>')

f_html.write('</table>')
f_html.write('</form>')