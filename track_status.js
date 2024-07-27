document.getElementById('trackForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let reportId = document.getElementById('reportId').value;
    fetch(`/track_status/${reportId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('statusResult').innerText = `Status: ${data.status}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('statusResult').innerText = 'Error retrieving status.';
    });
});
