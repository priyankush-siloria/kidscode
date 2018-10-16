
import boto3
from botocore.exceptions import ClientError


SENDER = "learn@skoolofcode.com"

# RECIPIENTS = []

AWS_REGION = "us-west-2"

# SUBJECT = "Testing"

# BODY_TEXT = ("Amazon SES Test (Python)\r\n"
#              "This email was sent with Amazon SES using the "
#              "AWS SDK for Python (Boto)."
#             )
            
BODY_TEXT = ""
# BODY_HTML = """<html>
# <head></head>
# <body>
#   <h1>Amazon SES Test (SDK for Python)</h1>
#   <p>This email was sent with
#     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
#     <a href='https://aws.amazon.com/sdk-for-python/'>
#       AWS SDK for Python (Boto)</a>.</p>
# </body>
# </html>
#             """            

CHARSET = "UTF-8"

def awsMailSending(recipients,subject,body_html):
	client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id="AKIAJUV6HTEPNFQSVBYQ",aws_secret_access_key="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")

	try:
	    response = client.send_email(
	        Destination={
	            'ToAddresses': recipients
	        },
	        Message={
	            'Body': {
	                'Html': {
	                    'Charset': CHARSET,
	                    'Data': body_html,
	                },
	                'Text': {
	                    'Charset': CHARSET,
	                    'Data': BODY_TEXT,
	                },
	            },
	            'Subject': {
	                'Charset': CHARSET,
	                'Data': subject,
	            },
	        },
	        Source=SENDER,
	    )
	except ClientError as e:
	    print(e.response['Error']['Message'])
	    pass
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])