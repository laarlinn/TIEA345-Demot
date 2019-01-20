#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# Pin configurations
# Main traffic lights
LED_GREEN = 6
LED_RED = 4
LED_YELLOW = 5

# Pedestrian lights
LED_JK_GREEN = 20
LED_JK_RED = 21
LED_JK_YELLOW = 16
LED_JK_BUTTON = 26 # Pedestrian button
PIR_PIN = 12 # PIR sensor

LED_FLASHING_RATE = 0.5
PEDESTRIAN_TIME = 8

def init_gpio():
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_JK_GREEN, GPIO.OUT)
    GPIO.setup(LED_JK_RED, GPIO.OUT)
    GPIO.setup(LED_JK_YELLOW, GPIO.OUT)
    GPIO.setup(LED_JK_BUTTON, GPIO.IN)
    GPIO.setup(PIR_PIN, GPIO.IN)

def lights_normal_state():
    GPIO.output(LED_JK_GREEN, 0)
    GPIO.output(LED_JK_RED, 1)
    GPIO.output(LED_GREEN, 0)
    GPIO.output(LED_RED, 1)
    sleep(1)
    GPIO.output(LED_YELLOW, 1)
    sleep(1)
    GPIO.output(LED_RED, 0)
    GPIO.output(LED_YELLOW, 0)
    GPIO.output(LED_GREEN, 1)

def button_pressed():
    GPIO.output(LED_JK_YELLOW, 1)
    if GPIO.input(PIR_PIN) == 1:
        sleep(5)
    GPIO.output(LED_GREEN, 0)
    GPIO.output(LED_YELLOW, 1)
    sleep(1)
    GPIO.output(LED_YELLOW, 0)
    GPIO.output(LED_RED, 1)
    sleep(1)
    GPIO.output(LED_JK_RED, 0)
    GPIO.output(LED_JK_YELLOW, 0)
    GPIO.output(LED_JK_GREEN, 1)
    sleep(PEDESTRIAN_TIME)
    GPIO.output( LED_JK_GREEN, 0)
    sleep(LED_FLASHING_RATE)
    GPIO.output(LED_JK_GREEN, 1)
    sleep(LED_FLASHING_RATE)
    GPIO.output(LED_JK_GREEN, 0)
    sleep(LED_FLASHING_RATE)
    GPIO.output(LED_JK_GREEN, 1)
    sleep(LED_FLASHING_RATE)

def main():
    init_gpio() 
    try:
        # Setting the lights to the normal state
        lights_normal_state()
        # Main loop
        while True:
            if GPIO.input(LED_JK_BUTTON) == 1:
                button_pressed()
                lights_normal_state()
            sleep(0.1)
    except KeyboardInterrupt:
        print "Stopping..."
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()