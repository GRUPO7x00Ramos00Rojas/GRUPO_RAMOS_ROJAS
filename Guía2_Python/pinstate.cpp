#include <wiringPi.h>
#include <iostream>

int main() {
    if (wiringPiSetupGpio() == -1) {
        std::cerr << "Failed to initialize WiringPi." << std::endl;
        return 1;
    }

    int pinNumber = 17;  // Replace with the GPIO pin number you want to check.
    pinMode(pinNumber, INPUT);

    int state = digitalRead(pinNumber);

    if (state == HIGH) {
        std::cout << "Pin is HIGH." << std::endl;
    } else {
        std::cout << "Pin is LOW." << std::endl;
    }

    return 0;
}
