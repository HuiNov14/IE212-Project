function callPredictAPI() {
    fetch('http://127.0.0.1:5000/predict', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        updateTableWithResults(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

function updateTableWithResults(results) {
    var tableBody = document.querySelector('#resultTable tbody');
    clearTable(tableBody);
    populateTable(tableBody, results);
}

function clearTable(tableBody) {
    tableBody.innerHTML = ''; 
}

function populateTable(tableBody, results) {
    for (var i = 0; i < results.length; i++) {
        var labels = results[i].labels;

        var newRow = tableBody.insertRow();
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);

        cell1.textContent = i + 1;
        cell2.textContent = results[i].text;

        for (var j = 0; j < labels.length; j++) {
            var labelValue = labels[j][2];
            var labelColor = getLabelColor(labelValue);

            var labelRow = cell3.appendChild(document.createElement("div"));
            labelRow.textContent = labelValue.split("#")[0]; 

            labelRow.style.color = labelColor;
        }
    }
}

function getLabelColor(labelValue) {
    var color;
    if (labelValue.includes("#POSITIVE")) {
        color = "green";
    } else if (labelValue.includes("#NEGATIVE")) {
        color = "red";
    } else {
        color = "black";
    }
    return color;
}

document.getElementById('runModelBtn').addEventListener('click', callPredictAPI);