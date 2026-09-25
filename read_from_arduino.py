"""Read comma-separated flex-sensor values from an Arduino serial port."""

import argparse
import serial

from flex_to_num import flex_to_num


def read_from_arduino(serial_port: str, baud_rate: int = 9600):
    """Read one serial line, classify its sensor values, and return its label."""
    with serial.Serial(serial_port, baud_rate, timeout=2) as connection:
        line = connection.readline().decode("utf-8", errors="strict").strip()

    if not line:
        raise TimeoutError(f"No data received from {serial_port}.")

    try:
        sensor_values = [int(value.strip()) for value in line.split(",")]
    except ValueError as exc:
        raise ValueError(f"Expected comma-separated integer values; received {line!r}.") from exc

    result = flex_to_num(sensor_values)
    print(f"Received data: {sensor_values} -> predicted class: {result}")
    return result


def main() -> None:
    """Read and classify one value from the configured serial port."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("serial_port", help="Arduino serial port, e.g. COM6 or /dev/ttyACM0")
    parser.add_argument("--baud-rate", type=int, default=9600)
    args = parser.parse_args()
    print(f"Predicted class: {read_from_arduino(args.serial_port, args.baud_rate)}")


if __name__ == "__main__":
    main()
