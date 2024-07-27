document.getElementById('reportForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData(this);
    fetch('/submit_report', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('Issue reported successfully!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error reporting the issue.');
    });
});
