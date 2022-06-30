const int RELAY_ENABLE = 7;//CONNECT IN1 PIN OF RELAY TO ARDUINO PIN 7
int flag=0, cnt=0;
void setup() {                                             
                               
  pinMode(RELAY_ENABLE, OUTPUT);//POWER OUT FROM PIN 7(AS ABOVE DEFINED)
  pinMode(2, INPUT);//POWER INPUT IN PIN 2
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(2)==LOW)//SENSOR DETECT THE OBJECT
  {
    digitalWrite(7, LOW);//RELAY SWITCH TURNS ON SO FAN ON
 
    cnt=cnt+1;//COUNT OBJECT OCCURENCE
    delay(500);
    Serial.println(cnt) ;
  }
  if(cnt%2==0)//HERE OBJECT OCCURENCE IS IN MULTIPLE OF TWO THEN TURN SWITCH OFF(FAN OFF)
  {
    digitalWrite(7, HIGH);//RELAY  SWITCH TURNS OFF(FAN OFF)
  }
  else
  {
    digitalWrite(7, LOW);//RELAY SWITCH TURNS ON(FAN ON)
  }
 
}
