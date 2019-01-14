function exportTableToCSV(filename) {
    var csv = [];
    var rows = document.querySelectorAll("table tr");
    var header = document.querySelectorAll("table th");
//    console.log('Rows length = ' + rows.length)
    var headerlength = document.getElementById('tblCustomers').getElementsByTagName('th').length;
//    console.log("Header length :" + headerlength)
    var cols = document.getElementById('tblCustomers').getElementsByTagName('td'), colslen = cols.length, i = 0;
    var input = "";
//    for (var i = 0; i < rows.length; i++) {
//        var row = [], cols = rows[i].querySelectorAll("td, th");
//        console.log('Columns length = ' + cols.length)
////        for (var j = 0; j < cols.length; j++)
//        var j = 0
//        while (++j<cols.length){
//            console.log("Outside if = " + j)
//            if (j%8 == 0){
//                console.log("Inside if = " + j)
////                row.push(cols[j].children.inputbox.value)
//                  row.push(document.getElementById(j+1).children.inputbox.value)
//            }
//            else
//                row.push(cols[j].innerText);
//        }
//        console.log("Before loop = " + input)
        var j = -1
        while (++j < headerlength){
//        console.log(j)
        if (j == headerlength - 1) {
//            console.log("Header rows: "+ document.getElementsByTagName("th")[j].innerHTML)
//            console.log("Header rows: "+ document.getElementsByTagName("th")[j])
//            console.log("Value of j:" + j)
            input += document.getElementsByTagName("th")[j].innerHTML + '\n';
            }
        else{
            input += document.getElementsByTagName("th")[j].innerHTML + ",";
//              console.log(document.getElementsByTagName("th")[j].innerHTML)
            }
        }
        var i = 0
    	while(++i <= colslen){
            console.log("i = " + i);
            if (i%headerlength==0){
//                console.log(i)
                input += document.getElementById(i).children.inputbox.value + '\n';
//          input += '\n';
//            console.log("Inside IF Input = " + input);
//            console.log(document.getElementById("inputbox").value);
//            console.log(input.getElementsByTagName("input").children.value);
                                }
        else {
            input += document.getElementById(i).innerHTML + ",";
//            console.log("Else Input =" + input)
//            console.log(document.getElementById(i).innerHTML);
        }
//        csv.push(input.join(","));
//          input += ","
        }
    inputvalidation(this);

    // Download CSV file
    downloadCSV(input +="\n", "project.csv");
}

function downloadCSV(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV file
    csvFile = new Blob([csv], {type: "text/csv"});

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Hide download link
    downloadLink.style.display = "none";

    // Add the link to DOM
    document.body.appendChild(downloadLink);

    // Click download link
    downloadLink.click();
}

function inputvalidation( theForm ){
    var cols = document.getElementById('tblCustomers').getElementsByTagName('td'), colslen = cols.length, i = 0;
    var headerlength = document.getElementById('tblCustomers').getElementsByTagName('th').length;
    console.log(colslen);

    while (++i<colslen){
        if (i%headerlength==0){
                console.log(document.getElementById(i).children.inputbox.value);
                var regex = /^[a-zA-Z0-9/\\._]*$/;

                if (!regex.test(document.getElementById(i).children.inputbox.value))
                {
                    alert("Input field only takes A-Z, 0-9, and the following special characters '/','\','.','_'");
                }

            return !regex.test(document.getElementById(i).children.inputbox.value);
        }
    }
}