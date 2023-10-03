#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

channel = 11 # GPIO

GPIO.setmode(GPIO.BOARD) # Set which board

GPIO.setup(channel, GPIO.OUT) # Set channel and pin method

# Create a PWM object with a frequency of 100 Hz
pwm = GPIO.PWM(channel, 100)
pwm.start(0)

try:
    while True:
        # increase brightness
        for duty_cycle in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty_cycle)
            print(f"Increasing intensity: {duty_cycle}")
            time.sleep(0.1)
        
        # decrease brightness
        for duty_cycle in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty_cycle)
            print(f"Decreasing intensity: {duty_cycle}")
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()