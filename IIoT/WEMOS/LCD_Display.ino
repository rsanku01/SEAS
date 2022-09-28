#include <LiquidCrystal.h>
LiquidCrystal lcd(D8,D9,D4,D5,D6,D7);

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);

}

void loop() {
  
  int potentiometer = analogRead(A0);
  float voltage = 3.3*(potentiometer/1023.0);
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Voltage:");
  lcd.setCursor(0,1);
  lcd.print(voltage);
  delay(2000);
  

}
