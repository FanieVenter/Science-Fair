#include <TimeLib.h>
int thrust = 0;
int time = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  get_thrust();
  time = now();
  sendValues();
  delay(100);
}

void get_thrust() {
  thrust = analogRead(A1);
}

void sendValues() {
  String builtString = String("");
  builtString += String((int)time);
  builtString += String("|");
  builtString += String((int)thrust);
  Serial.println(builtString);
}
