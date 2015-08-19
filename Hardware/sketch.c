#include "IRremote.h"

int irrecvPin = 11;

IRrecv irrecv(irrecvPin);
decode_results results;

/**
** Connect to serial.
** Enable IR input
**/
void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
}

/**
** Listen for IR console data
** Write it to serial port
**/
void loop()
{
  if (irrecv.decode(&results))
  {
    Serial.println(results.value, HEX);
    irrecv.resume();
  }
}