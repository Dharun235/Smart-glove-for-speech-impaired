"""Run the serial-controlled SHWASI gesture-selection loop."""

import argparse
import time

import serial

from read_from_arduino import read_from_arduino


MODE_LABELS = {
    1: ["Stop", "Good Morning", "Good Afternoon", "Good Evening", "Good Night", "Hi! I am", "What’s your name?", "I am from", "MODE 1", "Nice to meet you", "What do you do?", "I am", "MODE 2", "Can you come again", "MODE 3", "On", "Please", "I am sorry", "Thank You", "Excuse me", "What do you think?", "That sounds great", "That smells good", "Never mind", "I don’t understand", "What do you mean?", "Can I help you", "How much does it cost", "I will be with you in a moment", "Please call me back", "My phone number is", "Have a good day"],
    2: ["Stop", "A", "B", "C", "D", "E", "F", "G", "MODE 1", "H", "I", "J", "MODE 2", "K", "MODE 3", "On", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""],
    3: ["Stop", "0", "1", "2", "3", "4", "5", "6", "MODE 1", "7", "8", "9", "MODE 2", "!", "MODE 3", "On", "#", "$", "%", "^", "&", "*", "(", ")", "-", "", "=", "+", "~", ".", ",", "<"],
}
MODE_SELECTORS = {9: 1, 13: 2, 15: 3}


def send_text(connection: serial.Serial, message: str) -> None:
    """Send UTF-8 text followed by a newline."""
    connection.write(f"{message}\n".encode("utf-8"))


def select_mode(sensor_port: str, output: serial.Serial, mode: int, baud_rate: int) -> bool:
    """Read one mode until mode change or stop; return whether to continue."""
    labels = MODE_LABELS[mode]
    while True:
        time.sleep(1)
        send_text(output, "Enter the value")
        print("Enter gesture number (1-32), or select another mode/0 to stop:")
        value = read_from_arduino(sensor_port, baud_rate)
        if value == 0:
            send_text(output, "Stopped.")
            return False
        if value in MODE_SELECTORS and MODE_SELECTORS[value] != mode:
            send_text(output, f"Exit - Mode {mode}")
            return True
        if 1 <= value <= len(labels):
            send_text(output, labels[value - 1])
            print(labels[value - 1])
        else:
            print(f"Invalid gesture number: {value}")


def run(sensor_port: str, output_port: str, baud_rate: int) -> None:
    """Run start/stop and mode-selection control flow."""
    with serial.Serial(output_port, baud_rate, timeout=2) as output:
        while True:
            send_text(output, "Start or stop")
            print("Enter 16 to start or 0 to stop:")
            start_input = read_from_arduino(sensor_port, baud_rate)
            if start_input == 0:
                send_text(output, "Stopped.")
                continue
            if start_input != 16:
                print("Invalid input. Enter 16 to start or 0 to stop.")
                continue

            send_text(output, "Started.")
            print("Started.")
            while True:
                time.sleep(1)
                send_text(output, "Enter the mode")
                print("Enter 9 for Mode 1, 13 for Mode 2, 15 for Mode 3, or 0 to stop:")
                selection = read_from_arduino(sensor_port, baud_rate)
                if selection == 0:
                    send_text(output, "Stopped.")
                    return
                if selection in MODE_SELECTORS:
                    mode = MODE_SELECTORS[selection]
                    print(f"Switched to mode {mode}")
                    if not select_mode(sensor_port, output, mode, baud_rate):
                        return


def main() -> None:
    """Parse serial-port options and start the control loop."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sensor-port", default="COM6")
    parser.add_argument("--output-port", default="COM5")
    parser.add_argument("--baud-rate", type=int, default=9600)
    args = parser.parse_args()
    run(args.sensor_port, args.output_port, args.baud_rate)


if __name__ == "__main__":
    main()
