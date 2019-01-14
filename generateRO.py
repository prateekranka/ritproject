import csv
# import sys

# Open the CSV file for reading
# reader = csv.reader(open(sys.argv[1]))
# datadict_path = 'C:\Users\USER\Downloads\RIT\Deliverables\\'
# reader = csv.reader(open(datadict_path + 'Inv_DataDictionary_Table.csv'))

reader = csv.reader(open('RepairOrders_DataDictionary_Table.csv'))

# Create the HTML file
# f_html = open(sys.argv[2],"w");
f_html = open('RepairOrders.html',"w")

f_html.write('<title>Fixed Operations</title>')

f_html.write('<head>')
# f_html.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
f_html.write('<meta name="viewport" http-equiv="Content-Type" content="width=device-width, initial-scale=1; text/html; charset=utf-8"/>')
f_html.write('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
f_html.write('<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">')
f_html.write('<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">')
f_html.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">')
f_html.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>')
# f_html.write('<script src = "rowcount.js"></script>')
# f_html.write('<script src="submit_javascript.js"></script>')
f_html.write('</head>')

f_html.write('<body>')
# f_html.write('<h1>Customer Onboarding Form</h1>')
# f_html.write('<h2>Inventory</h2>')
f_html.write('<style>body {background-color: white;text-align: center; font-family: "Roboto", sans-serif} table, th, td, input {    border: 1px solid black;    border-collapse: collapse; padding: 5px;} th, td {text-align: center} tr:hover{background-color: #f5f5f5} tr:nth-child(even) {background-color: #f2f2f2;} th {background-color: #4CAF50;color: white;} table.center{margin-left: auto; margin-right:auto} .w3-bar-block .w3-bar-item{padding:16px;font-weight:bold}</style>')
# f_html.write('<nav class="w3-sidebar w3-bar-block w3-collapse w3-animate-left w3-card" style="z-index:3;width:250px;" id="mySidebar">')

f_html.write('<nav class="w3-sidebar w3-bar-block w3-collapse w3-animate-left w3-card" style="z-index:3;width:250px;" id="mySidebar">')
# f_html.write('  <a class="w3-bar-item w3-button w3-border-bottom w3-large" href="#"><img src="https://www.w3schools.com/images/w3schools.png" style="width:80%;"></a>')
f_html.write('  <a class="w3-bar-item w3-button w3-hide-large w3-large" href="javascript:void(0)" onclick="w3_close()">Close <i class="fa fa-remove"></i></a>')
f_html.write('  <a class="w3-bar-item w3-button w3-teal" href="#">Home</a>')
f_html.write('  <a class="w3-bar-item w3-button" href="#">Inventory</a>')
f_html.write('  <a class="w3-bar-item w3-button" href="#">Variable Ops</a>')
f_html.write('  <a class="w3-bar-item w3-button" href="#">Fixed Ops</a>')
# f_html.write('  <a class="w3-bar-item w3-button" href="#">Link 4</a>')
# f_html.write('  <a class="w3-bar-item w3-button" href="#">Link 5</a>')
f_html.write('  <div>')
# f_html.write('    <a class="w3-bar-item w3-button" onclick="myAccordion("demo")" href="javascript:void(0)">Dropdown <i class="fa fa-caret-down"></i></a>')
f_html.write('    <div id="demo" class="w3-hide">')
f_html.write('      <a class="w3-bar-item w3-button" href="#">Link</a>')
# f_html.write('      <a class="w3-bar-item w3-button" href="#">Link</a>')
# f_html.write('      <a class="w3-bar-item w3-button" href="#">Link</a>')
f_html.write('    </div>')
f_html.write('  </div>')
f_html.write('</nav>')

f_html.write('<div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" id="myOverlay"></div>')

f_html.write('<div class="w3-main" style="margin-left:250px;">')

f_html.write('<div id="myTop" class="w3-container w3-top w3-theme w3-large">')
f_html.write('  <p><i class="fa fa-bars w3-button w3-teal w3-hide-large w3-xlarge" onclick="w3_open()"></i>')
f_html.write('  <span id="myIntro" class="w3-hide">Customer Onboarding Form: Fixed Ops</span></p>')
f_html.write('</div>')

f_html.write('<header class="w3-container w3-theme" style="padding:64px 32px">')
f_html.write('  <h1 class="w3-xxxlarge">Customer Onboarding Form</h1>')
f_html.write('  <h2 class="w3-large">Inventory</h2>')
f_html.write('</header>')


# reader.seek(0)
# f_html.seek(0)
f_html.write('<form method = "post" id = "form_id" name = "FORM">')

f_html.write('<div id = "dvData">')
f_html.write('<table id = "tblCustomers" class = "center">')
# f_html.seek(0)
for row in reader:
    for column in row:
        f_html.write('<th>' + column + '</th>')
    break
i = 1
for row in reader: # Read a single row from the CSV file
  # f_html.write('<div class = "tooltip"><span class = "tooltiptext"><tr>')# Create a new row in the table
  f_html.write('<tr>')
  for column in row: # For each column..
    if column == 'INPUT':
        f_html.write('<td id = "' + str(i) + '"><input TYPE="TEXT" NAME="inputbox" id ="inputbox" SIZE="20"></td>')
        # print i
        i+=1
        # print i
    else:
        f_html.write('<td id = "' + str(i) + '">' + column + '</td>')
        i+=1
  f_html.write('</tr>')
  # f_html.write('</div>')

f_html.write('</table>')
# f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "CountRows()"/>')
# f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "download_csv()"/>')
f_html.write('<input type = "button" name = "downloadbutton" value = "Download" onclick = "exportTableToCSV()"/>')
# f_html.write('<script src = "download_csv.js"></script>')
f_html.write('<script src = "downloadcsv.js"></script>')
f_html.write('<script src = "openclose.js"></script>')
# f_html.write('<script src = "rowcount.js"></script>')
f_html.write('</div>')
f_html.write('</form>')
f_html.write('</body>')