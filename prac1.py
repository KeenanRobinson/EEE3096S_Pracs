"""
Names: Keenan Robinson
Student Number: RBNKEE001
Prac: 1
Date: 26/07/2019
"""
# Program designed to in binary, displaying it using LEDs
# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools
#initialisations
GPIO.setmode(GPIO.BOARD)
#Pin numbers
# PLEASE NOTE THESE CONFIGURATIONS DIFFER TO CODE1.PY AND CODE.PY
BUTTON1=11	#Button to increase binary value
BUTTON2=7	#Button to decrease binary value
LED1=15
LED2=16
LED3=18
#Pin setups
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP) #pull up resistors
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#Variable initialisations
count = 0
binaryList = list(itertools.product([0,1], repeat=3))	#produces a list of potential binary values

def button_detect_increase(channel): #Interrupt ISR to increase binary count
    print('Falling Edge detected!')
    global count
    if count<7:
	count=count+1
	GPIO.output(LED1, binaryList[count][2])
	GPIO.output(LED2, binaryList[count][1])
	GPIO.output(LED3, binaryList[count][0])
    else:
	count=0 #Restarts counter back at 0
	GPIO.output(LED1, binaryList[count][2])
	GPIO.output(LED2, binaryList[count][1])
	GPIO.output(LED3, binaryList[count][0])

def button_detect_decrease(channel): #Interrupt ISR to decrease binary count
    print('Falling Edge detected!')
    global count
    if count>0:
	count=count-1
	GPIO.output(LED1, binaryList[count][2])
	GPIO.output(LED2, binaryList[count][1])
	GPIO.output(LED3, binaryList[count][0])
    else:
	count=7 #Adjusts counter to 8 
	GPIO.output(LED1, binaryList[count][2])
	GPIO.output(LED2, binaryList[count][1])
	GPIO.output(LED3, binaryList[count][0])

#Interrupt for when the button input detects a falling edge
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=button_detect_increase, bouncetime = 300)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=button_detect_decrease, bouncetime = 300)



# Logic that you write
def main():
    """ Code to turn the LED on and off with a 1 second delay
    GPIO.output(LED1,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED1,GPIO.LOW)
    time.sleep(1)
    """
    print("Binary value: "+str(count))
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



