#include <ArduinoJson.h>

void setup() 
{
    Serial.begin(9600);  
}

void loop() 
{
    DynamicJsonBuffer jsonBuffer;
  
    String input = "{\"dist\":[123,135,234,236],\"hum\":40,\"rfid\":\"0\",\"time\":1351824120,\"gps\":[48.756080,2.302038]}";
    
    JsonObject& root = jsonBuffer.parseObject(input);
  
    long time = root[String("time")];
  
    root[String("time")] = time;
    
    String output;
  
    root.printTo(output);

    Serial.println(output);

    delay(5000);
}
