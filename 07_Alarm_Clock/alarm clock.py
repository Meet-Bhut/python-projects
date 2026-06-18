import time
from datetime import datetime

while True:
    try:
        hour = int(input("Enter hour (0-23): "))

        if 0 <= hour <= 23:
            break

        print("Hour must be between 0 and 23")

    except ValueError:
        print("Please enter a valid number")


while True:
    try:
        minute = int(input("Enter minute (0-59): "))

        if 0 <= minute <= 59:
            break

        print("Minute must be between 0 and 59")

    except ValueError:
        print("Please enter a valid number")


print(f"\nAlarm set for {hour:02d}:{minute:02d}")

while True:
    current_time = datetime.now()
    print(current_time.strftime("%H:%M:%S"), end="\r")

    if current_time.hour == hour and current_time.minute == minute:
        print("\nWAKE UP!!!!!!! ⏰")
        break

    time.sleep(1)