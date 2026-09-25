// Collect one batch of five flex-sensor ADC readings as CSV.

const unsigned long SERIAL_BAUD = 9600;
const unsigned int SAMPLE_COUNT = 1000;

void setup() {
  Serial.begin(SERIAL_BAUD);
}

void loop() {
  for (unsigned int i = 0; i < SAMPLE_COUNT; ++i) {
    Serial.print(analogRead(A0));
    Serial.print(",");
    Serial.print(analogRead(A1));
    Serial.print(",");
    Serial.print(analogRead(A2));
    Serial.print(",");
    Serial.print(analogRead(A3));
    Serial.print(",");
    Serial.println(analogRead(A4));
  }

  // Reset board before collecting another batch.
  for (;;) {}
}
