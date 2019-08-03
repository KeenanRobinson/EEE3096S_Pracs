"""
Names: Keenan Robinson
Student Number: RBNKEE001
Prac: 1
Date: 26/07/2019
"""
# Program designed to toggle an LED off and on
# import Relevant Librares
import RPi.GPIO as GPIO
import time
#initialisations
GPIO.setmode(GPIO.BOARD)
#Pin numbers
LED1 = 11
BUTTON1=13
#Pin setups
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#Variable initialisations
high_pin = False

def button_detect(channel):
    print('Falling Edge detected!')
    global high_pin
    if high_pin==False:
    	GPIO.output(LED1, GPIO.HIGH)
	high_pin = True
        print('LED ON')
    else:
    	GPIO.output(LED1, GPIO.LOW)
	high_pin = False
	print('LED OFF')
#Interrupt for when the button goes to a low value
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=button_detect, bouncetime = 150)


# main function
def main():
    """ Code to turn the LED on and off with a 1 second delay
    GPIO.output(LED1,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED1,GPIO.LOW)
    time.sleep(1)
    """
    print("Waiting...")
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



