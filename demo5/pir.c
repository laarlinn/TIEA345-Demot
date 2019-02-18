#include <wiringPi.h>
#include <stdio.h>

#define LED 21
#define PIR 22

int main(void)
{
    wiringPiSetup();

    pinMode(LED, OUTPUT);
    pinMode(PIR, INPUT);

        for (;;)
    {
        if (digitalRead(PIR)) {
            digitalWrite(LED, 1);
        }
        else {
            digitalWrite(LED, 0);
        }
        delay(100);
    }
    return 0;
}
