void setup() {
  Serial.begin(9600); // Set the baud rate to match your Python script
}

void loop() {
  // Define the number of samples to collect
  const int num_samples = 1000;

  for (int i = 0; i < num_samples; ++i) {
    // Read five analog sensor values
    int sensorValue1 = analogRead(A0);
    int sensorValue2 = analogRead(A1);
    int sensorValue3 = analogRead(A2);
    int sensorValue4 = analogRead(A3);
    int sensorValue5 = analogRead(A4);

    // Print values to the serial monitor in CSV format
    Serial.print(sensorValue1);
    Serial.print(",");
    Serial.print(sensorValue2);
    Serial.print(",");
    Serial.print(sensorValue3);
    Serial.print(",");
    Serial.print(sensorValue4);
    Serial.print(",");
    Serial.println(sensorValue5);
  }

  // Stop the loop after collecting the specified number of samples
  while (1) {
    // Do nothing or perform any necessary tasks
  }
}
