#include<Arduino.h>
// Define the input and output pins
int xPin = 2;
int yPin = 3;
int zPin = 4;

// Define the state variable and set the initial state to S0
int state = 0;

void setup() {
  // Set the input and output pins
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  pinMode(zPin, OUTPUT);
}

void loop() {
  // Read the input pins
  int x = digitalRead(xPin);
  int y = digitalRead(yPin);

  // Determine the next state based on the current state and inputs
  switch (state) {
    case 0: // S0
      if (x == 1 && y == 0) {
        state = 1;
      }
      break;
    case 1: // S1
      if (x == 1 && y == 0) {
        state = 2;
      } else if (x == 0 && y == 1) {
        state = 3;
      }
      break;
    case 2: // S2
      if (x == 1 && y == 1) {
        state = 4;
        digitalWrite(zPin, HIGH);
      } else if (x == 0 && y == 1) {
        state = 3;
      }
      break;
    case 3: // S3
      if (x == 1 && y == 0) {
        state = 1;
      } else if (x == 1 && y == 1) {
        state = 4;
        digitalWrite(zPin, LOW);
      }
      break;
    case 4: // S4
      if (x == 1 && y == 0) {
        state = 1;
        digitalWrite(zPin, LOW);
      }
      break;
  }
  
  // Wait for a short time before reading inputs again
  delay(10);
}
