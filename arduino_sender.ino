
// Forward USB serial text to a Bluetooth serial link.

#include <SoftwareSerial.h>

const unsigned long SERIAL_BAUD = 9600;
// Pins 0 and 1 share USB serial on many Arduino boards; change if required.
SoftwareSerial BTserial(0, 1); // RX, TX

void setup() {
  Serial.begin(SERIAL_BAUD);
  BTserial.begin(SERIAL_BAUD);
}

void loop() {
  if (Serial.available() == 0) {
    return;
  }

  String command = Serial.readStringUntil('\n');
  command.trim();
  Serial.println(command);
  BTserial.println(command);
}
