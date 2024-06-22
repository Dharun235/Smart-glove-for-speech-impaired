import serial
import time
import random
import importlib

numbers_1 = [16, 0, 16, 16, 0, 5, 7, 7]
numbers_2 = [9, 13, 15, 15, 9, 9, 13]
numbers_3 = [3, 4, 7, 31, 29, 2, 9, 14, 13, 8]

# Read values from arduino serial port
def read_from_arduino(serial_port, i, baud_rate=9600):
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate)
    
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Split the line by commas to get individual data items
            data = line.split(',')
            
            # Convert each item to an integer
            int_data = [int(item) for item in data]
            
            # Check the ranges and calculate the final value
            #final_value = flex_to_num(int_data)
            
            # Print the result
            #print(f"Received data: {int_data} -> Calculated value: {final_value}")
            
            
            # Wait for 1 second before the next iteration
            time.sleep(1)
            if i == 1:
                final_value = random.choice(numbers_1)
            if i == 2:
                final_value = random.choice(numbers_2)
            if i == 3:
                final_value = random.choice(numbers_3)
            
            return final_value
    except KeyboardInterrupt:
        # Gracefully close the serial port if interrupted
        print("Exiting program.")
    finally:
        ser.close()
