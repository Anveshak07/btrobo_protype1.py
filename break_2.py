import time

# Simulated Motor Control Pins
in11 = "Motor 1 Forward"
in12 = "Motor 1 Backward"
in21 = "Motor 2 Forward"
in22 = "Motor 2 Backward"

def stop_motors():
    print("[STOP] Motors Stopped")

def move_forward():
    print(f"[FORWARD] {in11} ON, {in12} OFF, {in21} ON, {in22} OFF")

def move_backward():
    print(f"[BACKWARD] {in11} OFF, {in12} ON, {in21} OFF, {in22} ON")

def turn_left():
    print(f"[LEFT] {in11} OFF, {in12} ON, {in21} ON, {in22} OFF")

def turn_right():
    print(f"[RIGHT] {in11} ON, {in12} OFF, {in21} OFF, {in22} ON")

def main():
    print("Enter command (F: Forward, B: Backward, L: Left, R: Right, S: Stop, Q: Quit)")
    while True:
        command = input("Enter command: ").strip().upper()
        
        if command == 'F':
            move_forward()
        elif command == 'B':
            move_backward()
        elif command == 'L':
            turn_left()
        elif command == 'R':
            turn_right()
        elif command == 'S':
            stop_motors()
        elif command == 'Q':
            print("Exiting simulation.")
            break
        else:
            print("Invalid command, try again.")
        
        time.sleep(0.5)  # Simulating a delay

if __name__ == "__main__":
    main()

