import serial
import time
import importlib

# Read values from arduino serial port
def read_from_arduino(serial_port, baud_rate=9600):
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
            final_value = flex_to_num(int_data)
            
            # Print the result
            print(f"Received data: {int_data} -> Calculated value: {final_value}")   
            
            # Wait for 1 second before the next iteration
            time.sleep(1)
            return final_value
            
    except KeyboardInterrupt:
        # Gracefully close the serial port if interrupted
        print("Exiting program.")
        
    finally:
        ser.close()
