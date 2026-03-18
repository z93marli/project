#include <TM1637Display.h>

#define internal_led 13
#define CLK 4
#define DIO 3

TM1637Display display(CLK, DIO);

void setup ()
{
   pinMode(internal_led,OUTPUT); 
   display.setBrightness(3); // Sets the brightness level to 3
}

void loop()
{
   data[0]= display.encodeDigit(15); // This will display F___ on the display [0b01110001 = F]
	display.setSegments(data);
   digitalWrite(internal_led,HIGH);
   delay(50);
   digitalWrite(internal_led,LOW);
   delay(250);  
}
