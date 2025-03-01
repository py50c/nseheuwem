import time
import winsound  # For Windows beep sound

def study_timer(duration_minutes):
    # Convert minutes to seconds
    total_seconds = duration_minutes * 60

    print(f"Study timer started for {duration_minutes} minutes.")
    try:
        # Countdown
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            print(f"\r{minutes:02}:{seconds:02}", end="")
            time.sleep(1)
            total_seconds -= 1

        # Beep sound when countdown reaches zero
        print("\nTime's up! Beep!")
        winsound.Beep(1000, 1000)  # Frequency = 1000 Hz, Duration = 1000 ms (1 second)

    except KeyboardInterrupt:
        print("\nTimer stopped manually.")

# Get user input for study duration
try:
    duration = int(input("Enter the study duration in minutes: "))
    study_timer(duration)
except ValueError:
    print("Please enter a valid number.")
