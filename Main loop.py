import time
from read_from_arduino import read_from_arduino
import serial

# Define strings for each mode
mode1 = ["Stop", "Good Morning", "Good Afternoon", "Good Evening", "Good Night", "Hi! I am", "What’s your name?", "I am from", "MODE 1", "Nice to meet you", "What do you do?", "I am", "MODE 2", "Can you come again", "MODE 3", "On", "Please", "I am sorry", "Thank You", "Excuse me", "What do you think?", "That sounds great", "That smells good", "Never mind", "I don’t understand", "What do you mean?", "Can I help you", "How much does it cost", "I will be with you in a moment", "Please call me back", "My phone number is", "Have a good day"]

mode2 = ["Stop", "A", "B", "C", "D", "E", "F", "G", "MODE 1", "H", "I", "J", "MODE 2", "K", "MODE 3", "On", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]

mode3 = ["Stop", "0", "1", "2", "3", "4", "5", "6", "MODE 1", "7", "8", "9", "MODE 2", "!", "MODE 3", "On", "#", "$", "%", "^", "&", "*", "(", ")", "-", "", "=", "+", "~", ".", ",", "<"]


arduinoData2=serial.Serial('COM5',9600)


# Main loop starts
# First loop for checking 15 to start and 0 to stop
while True:
    arduinoData2.write("Start or stop")
    print("Enter 16 to start or 0 to stop: ")
    start_input = read_from_arduino('COM6',1)

    if start_input == 0:
        arduinoData2.write("Stopped.")
        print("Stopped.")
        continue
    
    elif start_input == 16:
        arduinoData2.write("Started.")
        print("Started.")
        
        # Second loop for getting mode and index
        while True:
            time.sleep(1)
            arduinoData2.write("Enter the mode")
            print("Enter 9 for Mode1  /n 13 for Mode2  /n 15 for Mode3 /n type '0' to stop: ")
            index =  read_from_arduino('COM6',2)     
            
            if index == 0:
                arduinoData2.write("Stopped.")
                print("Stopped.")
                break
        
            if index == 9:
                arduinoData2.write("Mode1")
                print("Switched to mode1")
                cont = True
                while cont:
                    time.sleep(1)
                    arduinoData2.write("Enter the value")
                    print("Enter the number for retrieving string, from 1 to 32: ")
                    index = read_from_arduino('COM6',3)
                    if index == 13 or index == 15:
                        arduinoData2.write("Exit - Mode1")
                        print("Exit from mode 1")
                        cont = False
                    elif index == 0:
                        break
                    else:
                        string = mode1[index-1]
                        arduinoData2.write(string)
                        print(f"{string}")
                if index == 0:
                    break
                
            if index == 13:
                print("Switched to mode2")
                cont = True
                while cont:
                    time.sleep(1)
                    arduinoData2.write("Enter the value")
                    print("Enter the number for retrieving string, from 1 to 32: ")
                    index = read_from_arduino('COM6',3)
                    if index == 9 or index == 15:
                        arduinoData2.write("Exit - Mode 2")
                        print("Exit from mode 2")
                        cont = False
                    elif index == 0:
                        break
                    else:
                        string = mode2[index-1]
                        arduinoData2.write(string)
                        print(f"{string}")
                if index == 0:
                    break
                
            if index == 15:
                print("Switched to mode3")
                cont = True
                while cont:
                    time.sleep(1)
                    arduinoData2.write("Enter the value")
                    print("Enter the number for retrieving string, from 1 to 32: ")
                    index = read_from_arduino('COM6',3)
                    if index == 13 or index == 9:
                        arduinoData2.write("Exit - mode 3")
                        print("Exit from mode 3")
                        cont = False
                    elif index == 0:
                        break
                    else:
                        string = mode3[index-1]
                        arduinoData2.write(string)
                        print(f"{string}")
                if index == 0:
                    break
                
    else:
        print("Invalid input. Please enter 16 to start or 0 to stop.")
    time.sleep(1)