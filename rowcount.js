var input;
function CountRows() {
    var totalRowCount = 0;
    var rowCount = 0;
    var columnCount = 0;
    var table = document.getElementById("tblCustomers");
    var rows = table.getElementsByTagName("tr");
    var cells = table.getElementsByTagName("td");
    var columns = (cells.length)/(rows.length-1);

//    console.log("Columns" + columns)
    console.log(rows[1].getElementsByTagName("td"));
//    console.log(rows)
//    console.log(rows[1].getElementsByTagName("td"))
//    console.log(rows[2].getElementsByTagName("td").id)
    for (var i = 0; i < rows.length; i++) {
        totalRowCount++;
        if (rows[i].getElementsByTagName("td").length > 0) {
            rowCount++;
//        for (var j = 0; rows[j].getElementsByTagName("/td").length  ""; j++)
//            columnCount++;
        }

//    for (var i = 0; i < rows.length; i++) {
//        var x = document.getElementById("").value;
//        document.getElementById("demo").innerHTML = x;
//        console.log(document.getElementById(i))
//    }
    }
//var j = 0
//var i = 1
//var k =0;
//console.log(rows.length)
//    for (var i = 1; i < rows.length; i++){
//        console.log("i = "+i)
//        for (var j = 0; j< columns; j++){
//            console.log("j = "+ j)
//            j += k
//            console.log("Inside loop k = "+ k)
//            console.log(document.getElementById(i+j).innerHTML)
//            console.log("i+j"+(i+j))
//            j += i
//        }
//        k = j
//        console.log("Out of loop k =" + k)
//    }


    var message = "Total Row Count: " + totalRowCount;
    message += "\nRow Count: " + rowCount + "\nColumn Count: "+ columnCount;
//    console.log(message)
//    alert(message);
//    document.getElementById("form_id").submit();
    var cols = document.getElementById('tblCustomers').getElementsByTagName('td'), colslen = cols.length, i = 0;
	while(++i < colslen){
        console.log("i = " + i);
        if (i%9==0){
            input += document.getElementById(i).children.inputbox.value;
            console.log("Input = " + input);
//            console.log(input.getElementById("inputbox").value);
//              console.log(input.getElementsByTagName("input").children.value);
        }
        else
            input += document.getElementById(i).innerHTML;
            console.log(document.getElementById(i).innerHTML);
        }
}

//function myFunction() {
////var x = document.getElementsByTagName("td").value;
////document.getElementById("demo").innerHTML = x;
//CountRows();
//}

function download_csv() {
    var data;
    CountRows();
    var csv = 'Name,Title\n';
    input.forEach(function(row) {
            csv += row.join(',');
            csv += "\n";
    });

    console.log(csv);
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
    hiddenElement.target = '_blank';
    hiddenElement.download = 'people.csv';
    hiddenElement.click();
}