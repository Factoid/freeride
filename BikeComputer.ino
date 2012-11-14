volatile unsigned long frame = 0;
volatile unsigned long lastTime = 0;

void setup()
{
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  attachInterrupt(0,stroke,FALLING);
}

void stroke()
{
  unsigned long time = millis();
  unsigned long delta = time - lastTime;
  if( delta > 70 )
  {
    lastTime = time;
    ++frame;
    Serial.print( frame );
    Serial.print( " " );
    Serial.println( time );
  }
}

void loop()
{
  digitalWrite(13, (millis() - lastTime < 10) );
}

