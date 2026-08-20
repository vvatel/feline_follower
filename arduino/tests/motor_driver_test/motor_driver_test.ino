#define STBY 8
#define AIN1 7
#define AIN2 6
#define PWMA 5
#define BIN1 9
#define BIN2 10
#define PWMB 11

void setup() {
  pinMode(STBY, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  
  digitalWrite(STBY, HIGH);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  analogWrite(PWMA, 150);

  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, 150);

  delay(2000);

  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
  delay(2000);
}