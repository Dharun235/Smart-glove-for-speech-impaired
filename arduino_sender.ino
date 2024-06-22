
String myCmd;
#include <SoftwareSerial.h>
SoftwareSerial BTserial(0, 1); // RX, TX
void setup() {
  Serial.begin(9600);
  BTserial.begin(9600);
}
void loop() {
 while(Serial.available()==0){
 }
 myCmd=Serial.readStringUntil('\r');
 Serial.println(myCmd);
 BTserial.println(myCmd);
 }
