#define internal_led 13


void setup ()
{
   pinMode(internal_led,OUTPUT);  
}

void loop()
{
   digitalWrite(internal_led,HIGH);
   delay(50);
   digitalWrite(internal_led,LOW);
   delay(250);  
}
