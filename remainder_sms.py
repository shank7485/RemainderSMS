from datetime import datetime
from pytz import timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(message, to_address):

    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("shank7485@yahoo.com","")

    fromaddr = "shank7485@yahoo.com"
    toaddr = "1" + to_address + "@tmomail.net"
    subject = "T Mobile Remainder"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

def get_time():
    current_time_CST = datetime.now(timezone('US/Central'))
    current_time_CST = (current_time_CST.strftime("%d %H")).split(" ")

    todays_date = current_time_CST[0]
    current_time_hour = current_time_CST[1]

    return current_time_hour, todays_date

def send_alert_message(hour, date):

    shashank1 = "4698261417"
    shashank2 = "4698261417"

    peoples = [shashank1,shashank2]

    if 7 <= date <= 9:
        # First Alert
        for person in peoples:
            send_email(' "Hi. This is a remainder to pay your T-mobile bill in a Week." ', person)

    elif 11 <= date <= 13:
        pass
        # Second Alert
        for person in peoples:
            send_email(' "Hi. This is a remainder to pay your T-mobile bill in 3 days." ', person)

    elif 14 <= date <= 15:
        pass
        # Final Alert
        for person in peoples:
            send_email(' "Hi. This is a remainder to pay your T-mobile bill ASAP." ', person)

    elif date == 16:
        pass
        # Final day Alert
        for person in peoples:
            send_email(' "Hi. "Please pay T mobile bill by today." ', person)

    elif date > 16:
        # Passed due date
        for person in peoples:
            send_email(' "Due date passed for T mobile bill. Pay it now!" ', person)

def main():
    time = get_time()
    send_alert_message(time[0], time[1])
    # send_alert_message(time[0], 8)

main()
