from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

app = FastAPI()

class IssueReport(BaseModel):
    department: str
    description: str
    location: str
    email: EmailStr
    file_url: str

@app.post("/report-issue/")
async def report_issue(issue: IssueReport, background_tasks: BackgroundTasks):
    # Simulate issue reporting
    # Here you can add logic to store the issue in a database or notify the relevant department
    background_tasks.add_task(send_email, issue.email)
    return {"message": "Issue reported successfully!"}

@app.post("/track-issue/")
async def track_issue(issue_id: str):
    # Simulate issue tracking
    # Here you can add logic to fetch the issue status from a database
    return {"status": "Your issue is being processed"}

def send_email(email: EmailStr):
    sender_email = "youremail@gmail.com"
    sender_password = "yourpassword"
    receiver_email = email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Issue Reported"
    msg.attach(MIMEText("Your issue has been reported successfully.", 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

def get_asset_location(gps_device_id):
    response = requests.get(f"https://api.gpsservice.com/devices/{gps_device_id}/location")
    return response.json()

@app.get("/get-location/")
async def get_location(gps_device_id: str):
    asset_location = get_asset_location(gps_device_id)
    return {"latitude": asset_location['latitude'], "longitude": asset_location['longitude']}
