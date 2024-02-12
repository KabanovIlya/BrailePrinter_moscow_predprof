const int dirPinx = 3;
const int stepPinx = 2;
const int dirPiny = 6;
const int stepPiny = 7;
const int stepsPerRevolution = 1499;
int isXDone = 0;
const int homeCoordsX = 200;
const int homeCoordsY = 4150;
int i = 0;
int currentx = 0;
int currenty = 0;
int isOnZero = 0;
int isOnHome = 0;
String incomingCommand = "";
#include <Servo.h>
Servo myservo;
void setup() {
  // put your setup code here, to run once:
  pinMode(stepPinx, OUTPUT);
  pinMode(5, INPUT_PULLUP);
  pinMode(dirPinx, OUTPUT);
    pinMode(stepPiny, OUTPUT);
  pinMode(4, INPUT_PULLUP);
  pinMode(dirPiny, OUTPUT);
  Serial.begin(9600);
  myservo.attach(10);
  myservo.write(160);
}
void gotoZero(){
  digitalWrite(dirPinx, LOW);
  digitalWrite(dirPiny, LOW);
  while(digitalRead(5))
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
  isXDone = 1;
  delay(1000);
  if(isXDone==1){
    while(digitalRead(4)){
        digitalWrite(stepPiny, HIGH);
        delayMicroseconds(500);
        digitalWrite(stepPiny, LOW);
        delayMicroseconds(500);
    }
  }
 isOnZero=1;
 isXDone=0;
}
void gotoHome(){
  digitalWrite(dirPinx, LOW);
  digitalWrite(dirPiny, LOW);
  while(digitalRead(5))
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
  isXDone = 1;
  delay(100);
  if(isXDone==1){
    digitalWrite(dirPinx, HIGH);
  for(int x = 0; x < homeCoordsX; x++)
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
    }
 isOnZero=1;
 isXDone=0;
   digitalWrite(dirPiny, LOW); // Установка вращения по часовой стрелки
 
      while(digitalRead(4)){
        digitalWrite(stepPiny, HIGH);
        delayMicroseconds(500);
        digitalWrite(stepPiny, LOW);
        delayMicroseconds(500);
    }
  delay(100);
  
  digitalWrite(dirPiny, HIGH); // Установка вращения против часовой стрелки
 
  for(int x = 0; x < homeCoordsY; x++)
  {
    digitalWrite(stepPiny, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPiny, LOW);
    delayMicroseconds(500);
  }
  isOnHome=1;
}
void nextDot(){
 digitalWrite(dirPinx, HIGH); // Установка вращения по часовой стрелки
  
  for(int x = 0; x < 20; x++)
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
  myservo.write(95);
  delay(300);
  myservo.write(160);
}
void nextNoDot(){
 digitalWrite(dirPinx, HIGH); // Установка вращения по часовой стрелки
  
  for(int x = 0; x < 20; x++)
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
}
void nextString(){
  digitalWrite(dirPinx, LOW);
  if(isXDone==0){
  while(digitalRead(5))
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
  }
  isXDone=1;
  int isX2Done = 0;
  if(isXDone==1){
       digitalWrite(dirPinx, HIGH); // Установка вращения по часовой стрелки
  
  for(int x = 0; x < homeCoordsX; x++)
  {
    digitalWrite(stepPinx, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPinx, LOW);
    delayMicroseconds(500);
  }
  isX2Done=1;
  }
  if(isX2Done==1){
  digitalWrite(dirPiny, LOW); // Установка вращения против часовой стрелки
 
  for(int x = 0; x < 40; x++)
  {
    digitalWrite(stepPiny, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPiny, LOW);
    delayMicroseconds(500);
  }
  }
  isXDone=0;
  isX2Done=0;
}
void loop() {
  if (isOnHome==0){
    gotoHome();
  }
  String data = Serial.readStringUntil('\n');
  if(data=="."){
    nextDot();
  }
  if(data=="-"){
    nextNoDot();
  }
  if(data=="*"){
    nextString();
  }
  if(data=="gohome"){
    gotoHome();
  }
}
