import requests

url = "https://toobaiqbal.app.n8n.cloud/webhook-test/920a7033-9fa8-4b88-afff-65f9b7b646d2"

data = {
    "intent": "property_search",
    "client_name": "Tooba",
    "phone": "03001234567",
    "property": "Faisalabad 10 Marla House",
    "appointment_date": "25 September 2026",
    "appointment_time": "4:00 PM",
    "status": "Booked",
    "employee": "Ahmed",
    "client_requirements": "Client wants to visit the property.",

    "conversation_transcript": "Client asked about a Faisalabad 10 Marla house and wanted to visit the property.",
    "appointment_history": "Appointment booked for 25 September 2026 at 4:00 PM.",
    "follow_up_reminder": "Follow up with client after property visit."
}

response = requests.post(
    url,
    json=data
)

print(response.status_code)
print(response.text)