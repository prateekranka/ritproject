import csv

reader = csv.reader(open('Inv_DataDictionary_Table.csv'))

f_html = open('Inventory.html',"w")

f_html.write('<title>Inventory</title>'
             '<head>'
             '<meta name="viewport" http-equiv="Content-Type" content="width=device-width, initial-scale=1; text/html; charset=utf-8"/>'
             '<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">'
             '<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">'
             '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">'
             '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
             '<script src="https://sdk.amazonaws.com/js/aws-sdk-2.7.16.min.js"></script>'
             '</head>'

             '<body>'
             '<style>body {background-color: white;text-align: center; font-family: "Roboto", sans-serif} table, th, td, input {    border: 1px solid black;    border-collapse: collapse; padding: 5px;} th, td {text-align: center} tr:hover{background-color: #f5f5f5} tr:nth-child(even) {background-color: #f2f2f2;} th {background-color: #4CAF50;color: white;} table.center{margin-left: auto; margin-right:auto} .w3-bar-block .w3-bar-item{padding:16px;font-weight:bold}</style>'

             '<nav class="w3-sidebar w3-bar-block w3-collapse w3-animate-left w3-card" style="z-index:3;width:250px;" id="mySidebar">'
             '<a class="w3-bar-item w3-button w3-hide-large w3-large" href="javascript:void(0)" onclick="w3_close()">Close <i class="fa fa-remove"></i></a>'
             '<a class="w3-bar-item w3-button w3-teal" href="#">Home</a>'
             '<a class="w3-bar-item w3-button" href="#">Inventory</a>'
             '<a class="w3-bar-item w3-button" href="#">Sales</a>'
             '<a class="w3-bar-item w3-button" href="#">Repair Orders</a>'

             '<div>'

             '<div id="demo" class="w3-hide">'
             '<a class="w3-bar-item w3-button" href="#">Link</a>'
             '</div>'

             '</div>'

             '</nav>'
             '<div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" id="myOverlay"></div>'
             '<div class="w3-main" style="margin-left:250px;">'
             '<div id="myTop" class="w3-container w3-top w3-theme w3-large">'
                '<p><i class="fa fa-bars w3-button w3-teal w3-hide-large w3-xlarge" onclick="w3_open()"></i>'
                '<span id="myIntro" class="w3-hide">Customer Onboarding Form: Inventory</span></p>'
            '</div>'

            '<header class="w3-container w3-theme" style="padding:64px 32px">'
            '<h1 class="w3-xxxlarge">Customer Onboarding Form</h1>'
            '<h2 class="w3-large">Inventory</h2>'
            '</header>')

# f_html.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
# f_html.write('<script src = "rowcount.js"></script>')
# f_html.write('<script src="submit_javascript.js"></script>')
# f_html.write('<h1>Customer Onboarding Form</h1>')
# f_html.write('<h2>Inventory</h2>')
# f_html.write('<nav class="w3-sidebar w3-bar-block w3-collapse w3-animate-left w3-card" style="z-index:3;width:250px;" id="mySidebar">')
# f_html.write('  <a class="w3-bar-item w3-button w3-border-bottom w3-large" href="#"><img src="https://www.w3schools.com/images/w3schools.png" style="width:80%;"></a>')
# f_html.write('  <a class="w3-bar-item w3-button" href="#">Link 4</a>')
# f_html.write('  <a class="w3-bar-item w3-button" href="#">Link 5</a>')
# f_html.write('    <a class="w3-bar-item w3-button" onclick="myAccordion("demo")" href="javascript:void(0)">Dropdown <i class="fa fa-caret-down"></i></a>')
# f_html.write('      <a class="w3-bar-item w3-button" href="#">Link</a>')
# f_html.write('      <a class="w3-bar-item w3-button" href="#">Link</a>')
# f_html.write('<div id="myTop" class="w3-container w3-top w3-theme w3-large">')
# f_html.write('  <p><i class="fa fa-bars w3-button w3-teal w3-hide-large w3-xlarge" onclick="w3_open()"></i>')
# f_html.write('  <span id="myIntro" class="w3-hide">Customer Onboarding Form: Inventory</span></p>')
# f_html.write('</div>')
#
# f_html.write('<header class="w3-container w3-theme" style="padding:64px 32px">')
# f_html.write('  <h1 class="w3-xxxlarge">Customer Onboarding Form</h1>')
# f_html.write('  <h2 class="w3-large">Inventory</h2>')
# f_html.write('</header>')


# reader.seek(0)
# f_html.seek(0)
f_html.write('<form method = "post" id = "form_id" name = "FORM">'
                '<div id = "dvData">'
                '<table id = "tblCustomers" class = "center">')
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
        # if
        f_html.write('<td id = "' + str(i) + '"><input TYPE="TEXT" NAME="inputbox" id ="inputbox" SIZE="20"></td>')
        # print i
        i+=1
        # print i
    else:
        f_html.write('<td id = "' + str(i) + '">' + column + '</td>')
        i+=1
  f_html.write('</tr>')
  # f_html.write('</div>')

f_html.write('</table>'
             '<input id="createTableButton" type="button" value="Create Table" onclick="createMovies()" />'
                '<br><br>'
                '<textarea readonly id= "textarea" style="width:400px; height:800px"></textarea>'
             '<input type = "button" name = "downloadbutton" value = "Download" onclick = "exportTableToCSV()"/>'
             '<script src = "downloadcsv.js"></script>'
             '<script src = "openclose.js"></script>'
             '<script src = "createTable.js"></script>'
             '</div>'
             '</form>'
             '</body>')
# f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "CountRows()"/>')
# f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "download_csv()"/>')
# f_html.write('<input type = "button" name = "downloadbutton" value = "Download" onclick = "exportTableToCSV()"/>')
# f_html.write('<script src = "download_csv.js"></script>')
# f_html.write('<script src = "rowcount.js"></script>')