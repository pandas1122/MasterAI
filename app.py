import openai
import requests

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    return message

def send_message(to_number, from_number, message):
    twilio_url = "https://api.twilio.com/2010-04-01/Accounts/<your-twilio-account-sid>/Messages.json"
    twilio_data = {
        "To": to_number,
        "From": from_number,
        "Body": message,
    }
    twilio_auth = ("ACe964526165f5440f62bb8c9a94e5c561", "509fdd5c354154b68a7b285e1a177468")
    requests.post(twilio_url, data=twilio_data, auth=twilio_auth)

def handle_message(from_number, message):
    response = generate_response(message)
    send_message(from_number, "+13134640406", response)
