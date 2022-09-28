
float PWM = 255.0;
float DT = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(D2, OUTPUT);
}

void loop() {
  
  float newPWM = PWM * DT;
  analogWrite(D2,newPWM);
  DT = DT + 0.2;
  
  
  delay(2000);
  
  if ( DT > 1)
  {
    DT = 0;
   }
    
}
