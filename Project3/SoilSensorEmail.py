import RPi.GPIO as GPIO
import smtplib
from email.message import EmailMessage
import time
import datetime

SENSOR_PIN = 4
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
SENDER_EMAIL = "1210604280@qq.com"
SENDER_PASSWORD = "hdhvdspujinfhgbb"
RECEIVER_EMAIL = "2070480071@email.com"


def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)


def read_sensor():
    return GPIO.input(SENSOR_PIN)


def send_email_notification(plant_status):
    msg = EmailMessage()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if plant_status == "DRY":
        msg['Subject'] = f'PLANT WATER ALERT {current_time}'
        body = "Soil is dry! Water needed immediately!\n\n"
    else:
        msg['Subject'] = f'Plant Status OK {current_time}'
        body = "Soil moisture is normal. No action needed.\n\n"

    body += f"Detection time: {datetime.datetime.now()}\n"
    body += "-- Raspberry Pi Plant Monitoring System"
    msg.set_content(body)

    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL


    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Email sending failed: {e}")
    finally:
        server.quit()


def main():

    try:

        setup_gpio()
        time.sleep(0.5)


        sensor_state = read_sensor()


        if sensor_state == GPIO.HIGH:
            print("Detected dry soil - Sending alert email")
            send_email_notification("DRY")
        else:
            print("Soil moisture normal - Sending status update")
            send_email_notification("MOIST")

    except Exception as e:
        print(f"System error: {e}")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()