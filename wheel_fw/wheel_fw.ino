/*
  Driver for the game controller steering wheel and brake/gas pedal unit
  
  Outputs a csv string 
  "shift_stick_up, shift_stick_down, brake_pedal, gas_pedal , steering wheel angle (-90 to +90)
  
  The first four vals are boolean - with 1 being an active high - the pedal/switch is pressed etc
*/

#define shift_up_pin 2
#define shift_down_pin 3
#define wheel_pin A0
#define accel_pin A1
#define brake_pin A2


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  
  pinMode(shift_up_pin, INPUT_PULLUP);
  pinMode(shift_down_pin, INPUT_PULLUP);

  pinMode(13, OUTPUT);   //ground for footpedal voltage dividers
  digitalWrite(13, LOW);

  pinMode(accel_pin, INPUT_PULLUP);
  pinMode(brake_pin, INPUT_PULLUP);
  
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  
  Serial.print(!digitalRead(shift_up_pin));
  Serial.print(",");
  Serial.print(!digitalRead(shift_down_pin));
  Serial.print(",");

  int accel_val = analogRead(accel_pin);
  if (accel_val < 200) accel_val=1;
  else accel_val=0;
  Serial.print(accel_val);
  Serial.print(",");


  int brake_val = analogRead(brake_pin);
  if (brake_val < 200) brake_val=1;
  else brake_val=0;
  Serial.print(brake_val);
  Serial.print(",");

  int wheel_val = analogRead(wheel_pin);
  int wheel_ang = map(wheel_val,0,1023,-90,90);
  Serial.print(wheel_ang);
  Serial.print("\n");


  
  
  delay(100);        // delay in between reads for stability
}
