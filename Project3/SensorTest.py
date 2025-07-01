import RPi.GPIO as GPIO
import time

SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    print("Soil Moisture Sensor Test")

    while True:
        moisture_level = GPIO.input(SENSOR_PIN)

        if moisture_level == GPIO.LOW:
            print("Status: Dry soil detected (no water needed)")
        else:
            print("Status: Moist soil detected (water needed)")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    GPIO.cleanup()