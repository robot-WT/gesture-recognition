/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be PORTD pins; 
  //otherwise additional changes in the code are required
  #define LEFT_ENC_PIN_A 5  //pin 2
  #define LEFT_ENC_PIN_B 8  //pin 3
  
  //below can be changed, but should be PORTC pins
  #define RIGHT_ENC_PIN_A 9  //pin A4
  #define RIGHT_ENC_PIN_B 7   //pin A5
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();

