// C++ code
//
int buttonState = 0;
int currButtonState, prevButtonState = LOW; // variable for reading the pushbutton status 
int ledState = LOW; 
const int buttonPin = 2;
const int ledPin = 13;
void setup()
{
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // read the state of the pushbutton
  currButtonState = digitalRead(buttonPin);
  if (currButtonState == HIGH && prevButtonState == LOW){
    ledState = !ledState;
    digitalWrite(ledPin, ledState);

  }
	prevButtonState	= currButtonState;
  
  delay(2); // Delay a little bit to improve simulation performance
}
