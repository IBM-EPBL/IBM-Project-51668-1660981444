const int buz=A1;
const int pir=A0;
const int lig=A2;
const int led=A3;
int a,b;
void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buz,OUTPUT);
  pinMode(pir,INPUT);
  pinMode(lig,INPUT);
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(pir,HIGH);
  digitalWrite(lig,HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(pir,LOW);
  digitalWrite(lig,LOW);
  delay(1000);
  a=analogRead(pir);
  b=analogRead(lig);
  if(a>0)
  {
    digitalWrite(buz,HIGH);
  }
  else 
  {
    digitalWrite(buz,LOW);
  }
  if(b<450)
  {
    digitalWrite(led,HIGH);
  }
  else 
  {
    digitalWrite(led,LOW);
  }

}