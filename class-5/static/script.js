function appendValue(value) {
    document.getElementById('result').value += value;
}

function clearDisplay() {
    document.getElementById('result').value = '';
}

function deleteLast() {
    let result = document.getElementById('result').value;
    document.getElementById('result').value = result.slice(0, -1);
}

function calculateResult() {
    let expression = document.getElementById('result').value;
    expression = expression.replace(/\^/g, '**');
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result) {
            document.getElementById('result').value = data.result;
        } else if (data.error) {
            document.getElementById('result').value = 'Error';
        }
    })
    .catch(error => {
        document.getElementById('result').value = 'Error';
    });
}
