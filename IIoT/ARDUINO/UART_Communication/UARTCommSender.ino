#include "Keyboard.h"
char Letter = 'r';
//char r;
int wait = 2;
int flag = 1;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  //char Letter = Serial.read();
  
    
  if (flag == 1)
  {
    Serial.print(Letter); 
    Serial.print(wait);
    flag = 0;
  }
  else
  {
    char ok = Serial.read();
    if (ok == 'o'){
    Serial.print(Letter); 
    Serial.print(wait); 
  }
  }
    
    
}
