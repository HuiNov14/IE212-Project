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
        var newRow = tableBody.insertRow();
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);
        cell1.textContent = i + 1;
        cell2.textContent = results[i].text;
        cell3.textContent = results[i].labels.map(label => label[2]).join(', ');
    }
}

document.getElementById('runModelBtn').addEventListener('click', callPredictAPI);