import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def SendEmail(report_file_path):
    try:
        SUBJECT = "Memory Utilization Report"
        text = """
        Hi,

        Please find attached the Memory Utilization Report:

        Thanks,
        Automation Team
        """
        
        sender_address = "balarcm2010@gmail.com"
        receiver_address = ['balamuralip93@gmail.com']

        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = sender_address
        msg['To'] = ", ".join(receiver_address)

        part1 = MIMEText(text, "plain")
        msg.attach(part1)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(report_file_path, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(report_file_path)}"')
        msg.attach(part)

        server = smtplib.SMTP("your_smtp_server_here", 25)
        # Replace "your_smtp_server_here" with your actual SMTP server address

        server.sendmail(sender_address, receiver_address, msg.as_string())
        server.quit()
        print("Email Sent Successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

# Call the SendEmail function with the report_fullpath as an argument
SendEmail(report_fullpath)
