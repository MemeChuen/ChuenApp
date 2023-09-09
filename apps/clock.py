import pytz
from datetime import datetime
import time


def local_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M %d %B %Y")
    print(f"It's currently {formatted_time}.")


def timezone():
    time_zone = input("Enter timezone: ")
    try:
        correct_timezone = pytz.timezone(time_zone)
        time_zone_time = datetime.now(correct_timezone)
        ftzt = time_zone_time.strftime("%H:%M %d %B %Y")
        ftzt2 = f"It's currently {ftzt} in {time_zone}."
        return ftzt2
    except pytz.UnknownTimeZoneError:
        print("Unknown Timezone")


def timer():
    while True:
        try:
            duration = int(input("Counts from (seconds): "))
            break
        except ValueError:
            print("Please enter a number.")
    while duration > 0:
        divmod(duration, 60)
        time.sleep(1)
        duration -= 1
    return "Times up!"


def clock():
    local_time()
    while True:
        option = input("Enter a command: ")
        if option == "/time":
            local_time()
        elif option == "/timezone":
            time_zone_now = timezone()
            print(time_zone_now)
        elif option == "/timezones":
            timezones = pytz.all_timezones
            print(timezones)
        elif option == "/timer":
            timesup = timer()
            print(timesup)
        elif option == "/exit":
            print("Exited")
            break
        else:
            print("Invalid Command")


clock()
