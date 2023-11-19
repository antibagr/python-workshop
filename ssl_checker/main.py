import ssl, socket
from datetime import datetime, date

from dateutil import parser
import boto3
from botocore.client import BaseClient
import os


access_key = "AKIAUCCEVLB5JCJSBGQO"
access_secret = "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"

# boto3.setup_default_session(profile_name="rudiemeant")
ses_client: BaseClient = boto3.client(
    "ses",
    region_name="eu-central-1",
    aws_access_key_id=access_key,
    aws_secret_access_key=access_secret,
)

IPS_TO_CHECK = [
    "www.yahoo.com:443",
    "www.microsoft.com:443",
    "www.google.com:443",
]


RESULT = []

BODY_TEXT_STR = []

for ip in IPS_TO_CHECK:
    address = ip.split(":")
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=address[0]) as s:
        s.connect((address[0], 443))
        cert = s.getpeercert()
        res = parser.parse(cert["notAfter"], fuzzy=True)
        current_day = date.today()
        days_left = (res.date() - current_day).days
        print(f"Checking certifcate for server {address[0]}")
        print(f"Expires on {res.date()} in {days_left} in days")
        RESULT.append({"server": address[0], "expirationdate": days_left})


# loop iterates through all the servers and checks if their exporation is in next 30 days. If true sends an email with the list of servers that are expiring in less than 30 days
for expiry in RESULT:
    if expiry["expirationdate"] < 60:
        BODY_TEXT_STR.append(
            f"Certificate for {expiry['server']} expires in {expiry['expirationdate']} days"
        )

if BODY_TEXT_STR:
    body_text = "\n".join(BODY_TEXT_STR)
    CHARSET = "UTF-8"
    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "hatehatehatehate.everything@gmail.com",  # Registered email in SES
            ],
        },
        Message={
            "Body": {"Text": {"Charset": CHARSET, "Data": body_text}},
            "Subject": {
                "Charset": CHARSET,
                "Data": "SSL certificate expiration",
            },
        },
        Source="rudiemeant@gmail.com",
    )
