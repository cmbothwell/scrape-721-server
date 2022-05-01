import sendgrid
import os

from dotenv import load_dotenv
import models

load_dotenv()

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
FROM_ADDRESS = "research@thresholdholdings.com"


def notify(recipient: str, job: models.Job) -> str:
    data = {
        "personalizations": [
            {
                "to": [{"email": recipient}],
                "subject": f'Your data request for your job "{job.name}" is complete',
            }
        ],
        "from": {"email": FROM_ADDRESS},
        "content": [
            {
                "type": "text/plain",
                "value": f'You can access "{job.name}" at the following link: {job.get_url()}',
            }
        ],
    }

    response = sg.client.mail.send.post(request_body=data)
    return response.status_code
