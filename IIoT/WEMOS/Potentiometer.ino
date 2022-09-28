

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int potentiometer = analogRead(A0);
  float voltage = 3.3*(potentiometer/1023.0);
  delay(1000);
  Serial.println(voltage);
  delay(2000);

}
