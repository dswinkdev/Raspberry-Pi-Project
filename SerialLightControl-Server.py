#------------------------------------------------------------------
# Change History
#------------------------------------------------------------------
# Version   |   Description
#------------------------------------------------------------------
#    1       |   Initial Development
#    2       |   Implemented state machine functionality as described
#------------------------------------------------------------------

# This imports the Python serial package to handle communications over the
# Raspberry Pi's serial port.
import serial

# Load the GPIO interface from the Raspberry Pi Python Module
# The GPIO interface will be available through the GPIO object
import RPi.GPIO as GPIO

# Original Serial and GPIO setup (as in the original code)
ser = serial.Serial(
        port='/dev/ttyS0',  # Serial port (ttyS0 on most Raspberry Pi boards)
        baudrate=115200,    # Baud rate (bits per second)
        parity=serial.PARITY_NONE,  # No parity bit
        stopbits=serial.STOPBITS_ONE,  # One stop bit for serial communication
        bytesize=serial.EIGHTBITS,    # 8 bits per byte
        timeout=1  # Timeout of 1 second for serial read operations
)

# GPIO Setup
GPIO.setwarnings(False)  # Disable warnings for GPIO
GPIO.setmode(GPIO.BCM)   # Use Broadcom GPIO pin numbering scheme
GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 18 as an output (for controlling an LED)

# Original repeat loop (keeps running until user exits or keyboard interrupt)
repeat = True

# Loop until the user hits CTRL-C or the client sends an exit/quit message
while repeat:
        # Read lines from the serial port 1 at a time.
        # This will block until we have data available.
        try:
                # Read a line from the serial port.
                # This also decodes the result into a utf-8 String (utf-8 is the
                # default North American English character set) and
                # normalizes the input to lower case.
                command = ((ser.readline()).decode("utf-8")).lower()

                # This is a state-machine implementation in Python.
                # We match on the value of a variable with individual 
                # cases used to represent each state. We can also build stateful
                # objects in python which we will study as we progress in 
                # this course.
                #
                # Please note, you can indicate multiple keys that represent the 
                # same state by using a pipe symbol to represent a boolean 'or'.
                #
                # The underscore symbol '_' is used to represent the default case
                # if nothing else matches in our list of cases.
                match command:
                        case "off":
                                # Set GPIO line 18 to False - disable output voltage
                                # This turns off voltage output to whatever may be 
                                # connected to GPIO line 18.
                                GPIO.output(18, False)

                        case "on":
                                # Set GPIO line 18 to True - enable output voltage
                                # This turns on voltage output to whatever may be 
                                # connected to GPIO line 18.
                                GPIO.output(18, True)

                        case "exit" | "quit":
                                # Cleanup the GPIO pins used in this application and 
                                # exit cleanly
                                GPIO.output(18, False)  # Turn off the LED
                                GPIO.cleanup()  # Cleanup GPIO settings
                                repeat = False  # Exit the loop

                        case _:
                                # No valid commands in the input so do nothing
                                pass

        except KeyboardInterrupt:
                # Exit cleanly when the user enters CTRL-C
                # Cleanup the GPIO pins used in this application and 
                # exit cleanly
                GPIO.output(18, False)
                GPIO.cleanup()
                repeat = False


# Updated State Machine Logic Implementation

# State machine states
STATE_OFF = "off"
STATE_ON = "on"
STATE_EXIT = "exit"
STATE_QUIT = "quit"
STATE_INVALID = "invalid"

# Configure our loop variable for updated state machine
repeat = True

# Function to handle different GPIO states
def set_gpio_state(state):
    """
    Set the state of the GPIO pin 18 based on the input command.
    
    Args:
    state (str): The state to set the GPIO pin to ('on', 'off').
    """
    if state == STATE_ON:
        GPIO.output(18, True)  # Turn on the LED
    elif state == STATE_OFF:
        GPIO.output(18, False)  # Turn off the LED
    else:
        print(f"Invalid state: {state}")  # Handle any invalid commands


# Main loop for updated state machine
while repeat:
    try:
        # Read a line from the serial port
        command = ser.readline().decode("utf-8").strip().lower()  # Get command and convert to lowercase

        # State machine logic to handle commands
        match command:
            case STATE_ON:
                # If the command is 'on', set GPIO pin to True (LED ON)
                set_gpio_state(STATE_ON)
                
            case STATE_OFF:
                # If the command is 'off', set GPIO pin to False (LED OFF)
                set_gpio_state(STATE_OFF)

            case STATE_EXIT | STATE_QUIT:
                # If the command is 'exit' or 'quit', clean up GPIO and exit the loop
                print("Exiting program...")
                GPIO.output(18, False)  # Ensure LED is turned off
                GPIO.cleanup()  # Cleanup the GPIO pins to reset their state
                repeat = False  # Exit the loop

            case _:
                # If the command is not recognized, print an error message
                print(f"Invalid command received: {command}")

    except KeyboardInterrupt:
        # Graceful exit on CTRL-C
        print("Program interrupted by user. Exiting...")
        GPIO.output(18, False)  # Turn off the LED before exiting
        GPIO.cleanup()  # Cleanup GPIO settings
        repeat = False  # Exit the loop
