
int receivedMessage;
int messageLength = 36;
double serialValues[68];
//test

void setup() {
  Serial.begin(28800);
  //Serial.flush();
}
void loop() {
  Serial.println("Test");
  if (Serial.available() >= messageLength) {      //From RPi to Arduino
    for (int i = 0; i <= messageLength; i++)
    {
    //  receivedMessage = receivedMessage * (Serial.read() - '0');  //converting the value of chars to integer
      serialValues[i] = receivedMessage;

    }
  
    Serial.println(serialValues);
    Serial.println("Test");
  }
}
