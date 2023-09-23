#include <Arduino.h>
#include <TimerOne.h>

#include <Servo.h>

Servo bigloopservo1;  // Create a servo object
Servo bigloopservo2;
Servo myservo1;
Servo myservo2;
Servo stopservo;


const int relay1Pin = 2; // Pin connected to Relay 1
const int mode0 = 45;
const int mode1 = 0;
const int up = 45;
const int down = 0;
const int interruptPin = 3;
volatile bool coming = 1;
// const int relay2Pin = 3; // Pin connected to Relay 2
// const int relay3Pin = 4; // Pin connected to Relay 3

unsigned long relay1StartTime = 0;
unsigned long relay2StartTime = 0;
const unsigned long relayDelay = 2000; // Delay in milliseconds for relay 1 and 2


unsigned int counter=0; // for ir sensor interrput

int inPin = 3;    // pushbutton connected to digital pin 7
int val = 0;      // variable to store the read value
int blockRunin = 0; //flag to block run for 10 seconds
int blockRunout = 0; //flag to block run for 10 seconds

void handleRelayDelays();
void blink();
void timerIsr();
void trainLoc();
void executeCommand(char command);

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Attach the servo to pin 9
  bigloopservo1.attach(9);
  bigloopservo2.attach(10);
  myservo1.attach(11);
  myservo2.attach(12);
  stopservo.attach(13);

  // Set relay pins as OUTPUT
  pinMode(relay1Pin, OUTPUT);

  
  // Initialize relays to LOW (off)
  digitalWrite(relay1Pin, LOW);


    //pinMode(inPin, INPUT);    // sets the digital pin 7 as input
    Timer1.initialize(1000000); // set a timer of length 1sec
    attachInterrupt(1, blink, CHANGE);  //INT0
    Timer1.attachInterrupt( timerIsr ); // attach the service routine here


}


void blink()
{
  int pinCurrent =  digitalRead(inPin);
  if ( pinCurrent == 1 && val == 0 && blockRunin == 0){
    Serial.println("out station");
    blockRunin = 2;


  }
   if (pinCurrent == 0 && val == 1 && blockRunout == 0){
    Serial.println("in station");
    blockRunout = 2;

    
  } 


  val = pinCurrent;
}
void timerIsr()
{
    Timer1.detachInterrupt();  //diable the timer1
    if (blockRunin > 0){
      blockRunin--;
    }
    if (blockRunout > 0){
      blockRunout--;
    }

    Timer1.attachInterrupt( timerIsr );  //enable the timer1
}



void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    executeCommand(command);
    //attachInterrupt(digitalPinToInterrupt(interruptPin), trainLoc(), CHANGE);
  }
  
  // Check and handle non-blocking relay delays
  handleRelayDelays();
}

void executeCommand(char command) {
  switch (command) {
    // case 'A':
    //   digitalWrite(relay1Pin, HIGH);
    //   relay1StartTime = millis();
    //   Serial.println("Command A executed");
    //   break;
    // case 'B':
    //   digitalWrite(relay2Pin, HIGH);
    //   relay2StartTime = millis();
    //   Serial.println("Command B executed");
    //   break;
    case 'R': //restart - the train is doing the big loop
      stopservo.write(down);
      bigloopservo1.write(mode0);
      bigloopservo2.write(mode0);
      Serial.println("Command Restart executed");
      break;
    case 'S': //stops the train
      stopservo.write(up);
      Serial.println("Command Stop executed");
      break;
    case 'H': //stops and shocks
      stopservo.write(up);
      Serial.println("Command Over-Time executed");
      digitalWrite(relay1Pin, HIGH);
      delay(2000);
      digitalWrite(relay1Pin, LOW);
      break;
    case '1': //enters small loop, option 1
      bigloopservo1.write(mode1);
      bigloopservo2.write(mode1);
      myservo1.write(mode1);
      myservo2.write(mode0); //one should go the opposite way
      Serial.println("Command 1 executed");
      break;
    case '2': //enters small loop, option 2
      bigloopservo1.write(mode1);
      bigloopservo2.write(mode1);
      myservo1.write(mode0);
      myservo2.write(mode1); //one should go the opposite way
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
  
  // if (digitalRead(relay2Pin) == HIGH && millis() - relay2StartTime >= relayDelay) {
  //   digitalWrite(relay2Pin, LOW);
  //}
}

void trainLoc(){
  if (coming == 1){
    coming = 0;
  }
  else{
    coming = 1;
  }
}