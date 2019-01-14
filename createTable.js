AWS.config.update({
  region: "us-east-2",
  endpoint: "http://localhost:8000",
  accessKeyID: "AKIAJ24WKTHKORNRJMRA",
  secretAccessKey: "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"
});

//var dynamodb = new AWS.DynamoDB();
var docClient = new AWS.DynamoDB.DocumentClient()

function createMovies() {

var table = "Submit_Button";
var year = 2015;
var title = "The Big New Movie";

// Update the item, unconditionally,

var params = {
    TableName:table,
    Key:{
        "submit_flag": "Inventory",
        "submit_Inv": "True",
    },
    ReturnValues:"UPDATED_NEW"
};

console.log("Updating the item...");

docClient.update(params, function(err, data) {
    if (err) {
        console.error("Unable to update item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
        console.log("UpdateItem succeeded:", JSON.stringify(data, null, 2));
    }
});
}