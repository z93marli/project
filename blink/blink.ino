#include <TM1637Display.h>

#define internal_led 13
#define CLK 4
#define DIO 3

TM1637Display display(CLK, DIO);

int x=0;

void setup ()
{
   pinMode(internal_led,OUTPUT); 
   display.setBrightness(1); // Sets the brightness level to 3
}

void loop()
{
   display.showNumberDec(x,0,4,0);
   delay (1000);
   x++;
   //display.clear();
}
