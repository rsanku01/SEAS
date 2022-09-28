char ok = 'o';
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(8,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    char Letter = Serial.read();
    int wait = Serial.parseInt();
    digitalWrite(8,HIGH);
    int randi = random(1,7);
    delay(randi*1000);
    Serial.print(ok);
    digitalWrite(8,LOW);
    delay(wait*1000);
    
    }
}
