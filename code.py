#!/usr/bin/python3
"""
Names: Keenan Robinson
Student Number: RBNKEE001
Prac: 1
Date: 26/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
#initialisations
GPIO.setmode(GPIO.BOARD)
LED1 = 11
GPIO.setup(LED1,GPIO.OUT, initial = GPIO.HIGH)		
#Pin 17 on raspberry connected to LED 1		
#initial state must be LOW

# Logic that you write
def main():
    GPIO.output(LED1,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED1,GPIO.HIGH)
    time.sleep(1)
    


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
