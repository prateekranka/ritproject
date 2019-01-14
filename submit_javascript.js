<script type = "text/javascript">
//function submit_by_id() {
//var name = document.getElementById("inout").value;
////var email = document.getElementById("email").value;
//if (validation()) // Calling validation function
//{
//document.getElementById("form_id").submit(); //form submission
////alert(" Name : " + name + " n Email : " + email + " n Form Id : " + document.getElementById("form_id").getAttribute("id") + "nn Form Submitted Successfully......");
//alert(" Name : " + name + " Form Id : " + document.getElementById("form_id").getAttribute("id") + "nn Form Submitted Successfully......");
//}
//}

function submit_data() {
    //document.getElementById("trial").innerHTML = "Hi";

    var myRows = [];
    var $headers = $("th");
    var $rows = $("tbody tr").each(function(index) {
      $cells = $(this).find("td");
      myRows[index] = {};
      $cells.each(function(cellIndex) {
        myRows[index][$($headers[cellIndex]).html()] = $(this).html();
      });
    });
    var myObj = {};
    myObj.myrows = myRows;

    //document.getElementById("demo").innerHTML = "Hello JavaScript!";
    document.getElementById("json").innerHTML = JSON.stringify(myObj);
    //document.getElementById("Try").innerHTML = "Hi";
}
</script>