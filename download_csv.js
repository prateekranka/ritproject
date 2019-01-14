//<script type='text/javascript' src='https://code.jquery.com/jquery-1.11.0.min.js'></script>
//<!-- If you want to use jquery 2+: https://code.jquery.com/jquery-2.1.0.min.js -->
//<script type='text/javascript'>
$(document).ready(function () {
    console.log("HELLO")
    function exportTableToCSV($table, filename) {
        var $headers = $table.find('tr:has(th)')
            ,$rows = $table.find('tr:has(td)')
            ,$input = $table.find('td:has(input)')
//            console.log($input[0].children.inputbox.value)
            // Temporary delimiter characters unlikely to be typed by keyboard
            // This is to avoid accidentally splitting the actual contents
            ,tmpColDelim = String.fromCharCode(11) // vertical tab character
            ,tmpRowDelim = String.fromCharCode(0) // null character
            // actual delimiter characters for CSV format
            ,colDelim = '","'
            ,rowDelim = '"\r\n"';
            // Grab text from table into CSV formatted string
            var csv = '"';
            csv += formatRows($headers.map(grabRow));
            csv += rowDelim;
            csv += formatRows($rows.map(grabRow)) + '"';
            csv += formatRows($input.map(grabRow)) + '"';
            console.log(csv)
            // Data URI
            var csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);
        // For IE (tested 10+)
        if (window.navigator.msSaveOrOpenBlob) {
            var blob = new Blob([decodeURIComponent(encodeURI(csv))], {
                type: "text/csv;charset=utf-8;"
            });
            navigator.msSaveBlob(blob, filename);
        } else {
            $(this)
                .attr({
                    'download': filename
                    ,'href': csvData
                    //,'target' : '_blank' //if you want it to open in a new window
            });
        }
        //------------------------------------------------------------
        // Helper Functions
        //------------------------------------------------------------
        // Format the output so it has the appropriate delimiters
        function formatRows(rows){
            return rows.get().join(tmpRowDelim)
                .split(tmpRowDelim).join(rowDelim)
                .split(tmpColDelim).join(colDelim);
        }
        // Grab and format a row from the table
        function grabRow(i,row){
            var input = $input[i];
            var $row = $(row);
            //for some reason $cols = $row.find('td') || $row.find('th') won't work...
            var $cols = $row.find('td');
            if(!$cols.length) $cols = $row.find('th');
//            if()
            return $cols.map(grabCol)
                        .get().join(tmpColDelim);
        }
        // Grab and format a column from the table
        function grabCol(j,col){
            var $col = $(col),
                $text = $col.text();
            return $text.replace('"', '""'); // escape double quotes
        }
    }
    // This must be a hyperlink
    $("#export").click(function (event) {
        // var outputFile = 'export'
        var outputFile = window.prompt("What do you want to name your output file (Note: This won't have any effect on Safari)") || 'export';
        outputFile = outputFile.replace('.csv','') + '.csv'

        // CSV
//        exportTableToCSV.apply(this, [$('#dvData > table'), outputFile]);
        exportTableToCSV.apply(this, [$('#dvData > table'), outputFile]);
        // IF CSV, don't do event.preventDefault() or return false
        // We actually need this to be a typical hyperlink
    });
});
//</script>