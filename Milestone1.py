#------------------------------------------------------------------
# Milestone1.py - Demonstrating PWM effects on an LED
#
# This code explores the effects of frequency and duty cycle changes
# using PWM to control LED brightness on a Raspberry Pi.
#------------------------------------------------------------------

import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Step 2: Change the PWM frequency and observe when the LED starts blinking
pwm18 = GPIO.PWM(18, 10)  # Starting with a low frequency of 10Hz
pwm18.start(50)  # Initial 50% duty cycle

print("Reducing PWM frequency. Observe when the LED starts blinking.")

try:
    for freq in range(10, 1, -1):  # Reduce frequency from 10Hz downward
        pwm18.ChangeFrequency(freq)  # Set new frequency
        time.sleep(2)  # Wait to observe the LED behavior
except KeyboardInterrupt:
    pwm18.stop()
    GPIO.cleanup()
    exit()

# Reset frequency to 60Hz for Step 3
pwm18.ChangeFrequency(60)

# Step 3: Change duty cycle to observe LED brightness changes
print("Reducing duty cycle. Observe brightness changes.")

try:
    for duty in range(50, 0, -5):  # Start at 50%, reduce in steps of 5%
        pwm18.ChangeDutyCycle(duty)
        time.sleep(2)  # Wait to observe changes
except KeyboardInterrupt:
    pwm18.stop()
    GPIO.cleanup()
    exit()

# Step 4 & 5: Fade the LED in and out continuously in a loop
print("Starting LED fade in and out...")

try:
    while True:
        # Fade in
        for duty in range(0, 101, 5):  # Increase brightness
            pwm18.ChangeDutyCycle(duty)
            time.sleep(0.1)
        
        # Fade out
        for duty in range(100, -1, -5):  # Decrease brightness
            pwm18.ChangeDutyCycle(duty)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping PWM and Cleaning Up")
    pwm18.stop()
    GPIO.cleanup()