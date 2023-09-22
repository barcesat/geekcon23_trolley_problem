#include <Servo.h>

Servo myservo;  // Create a servo object

const int relay1Pin = 2; // Pin connected to Relay 1
const int relay2Pin = 3; // Pin connected to Relay 2
const int relay3Pin = 4; // Pin connected to Relay 3

unsigned long relay1StartTime = 0;
unsigned long relay2StartTime = 0;
const unsigned long relayDelay = 2000; // Delay in milliseconds for relay 1 and 2

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Attach the servo to pin 9
  myservo.attach(9);

  // Set relay pins as OUTPUT
  pinMode(relay1Pin, OUTPUT);
  pinMode(relay2Pin, OUTPUT);
  pinMode(relay3Pin, OUTPUT);
  
  // Initialize relays to LOW (off)
  digitalWrite(relay1Pin, LOW);
  digitalWrite(relay2Pin, LOW);
  digitalWrite(relay3Pin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    executeCommand(command);
  }
  
  // Check and handle non-blocking relay delays
  handleRelayDelays();
}

void executeCommand(char command) {
  switch (command) {
    case 'A':
      digitalWrite(relay1Pin, HIGH);
      relay1StartTime = millis();
      Serial.println("Command A executed");
      break;
    case 'B':
      digitalWrite(relay2Pin, HIGH);
      relay2StartTime = millis();
      Serial.println("Command B executed");
      break;
    case 'R':
      digitalWrite(relay3Pin, HIGH);
      Serial.println("Command R executed");
      break;
    case 'S':
      digitalWrite(relay3Pin, LOW);
      Serial.println("Command S executed");
      break;
    case '1':
      myservo.write(0);
      Serial.println("Command 1 executed");
      break;
    case '2':
      myservo.write(180);
      Serial.println("Command 2 executed");
      break;
    default:
      Serial.println("Invalid command");
      break;
  }
}

void handleRelayDelays() {
  if (digitalRead(relay1Pin) == HIGH && millis() - relay1StartTime >= relayDelay) {
    digitalWrite(relay1Pin, LOW);
  }
  
  if (digitalRead(relay2Pin) == HIGH && millis() - relay2StartTime >= relayDelay) {
    digitalWrite(relay2Pin, LOW);
  }
}
