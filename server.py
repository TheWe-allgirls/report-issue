from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit_report', methods=['POST'])
def submit_report():
    # Process the form data
    department = request.form.get('department')
    description = request.form.get('description')
    location = request.form.get('location')
    file = request.files.get('file-upload')
    email = request.form.get('email')

    # Save the data to a database or process it as needed
    # ...

    # Send email notification
    # ...

    return jsonify({"message": "Report submitted successfully!"})

@app.route('/track_status/<report_id>', methods=['GET'])
def track_status(report_id):
    # Query the status from a database
    # ...
    status = "In Progress"  # Example status
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True)
