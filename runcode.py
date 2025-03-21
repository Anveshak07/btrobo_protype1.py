import RPi.GPIO as GPIO
import serial
import time

# Pin Definitions
in11 = 2  # Motor 1
in12 = 3  # Motor 1
in21 = 4  # Motor 2
in22 = 5  # Motor 2

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(in11, GPIO.OUT)
GPIO.setup(in12, GPIO.OUT)
GPIO.setup(in21, GPIO.OUT)
GPIO.setup(in22, GPIO.OUT)

# Serial communication (adjust port as needed)
ser = serial.Serial('/dev/ttyS0', 9600)  # Change to '/dev/ttyUSB0' if using USB

# Function to stop the motors initially
def stop_motors():
    GPIO.output(in11, 1)
    GPIO.output(in12, 1)
    GPIO.output(in21, 1)
    GPIO.output(in22, 1)

stop_motors()

print("Waiting for Bluetooth command...")

# Main loop
try:
    while True:
        if ser.in_waiting > 0:
            Buff = ser.read().decode('utf-8').strip()
            
            if Buff == 'F':  # Forward
                GPIO.output(in11, 1)
                GPIO.output(in12, 0)
                GPIO.output(in21, 1)
                GPIO.output(in22, 0)

            elif Buff == 'B':  # Backward
                GPIO.output(in11, 0)
                GPIO.output(in12, 1)
                GPIO.output(in21, 0)
                GPIO.output(in22, 1)

            elif Buff == 'L':  # Left
                GPIO.output(in11, 0)
                GPIO.output(in12, 1)
                GPIO.output(in21, 1)
                GPIO.output(in22, 0)

            elif Buff == 'R':  # Right
                GPIO.output(in11, 1)
                GPIO.output(in12, 0)
                GPIO.output(in21, 0)
                GPIO.output(in22, 1)

            elif Buff == 'S':  # Stop
                stop_motors()

            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()  # Reset GPIO on exit
    