#include <libserial/SerialStream.h>	//Librería puerto serial
#include <libserial/SerialPort.h>	//Librería puerto serial
#include <iostream>	//Librería estándar C
#include <fstream>	//Librería para manipulación de archivos
#include <vector>	//Librería para datos (buffer)
#include <sstream>	//Librería para convertir datos
#include <wiringPi.h> // Include the wiringPi library for GPIO access
#include <cstdlib>	//librería estándar de C++

using namespace LibSerial;
using namespace std;

int main()
{
    // Inicializa la librería wiringPi
    if (wiringPiSetupGpio() == -1)
    {
        cerr << "Failed to initialize wiringPi." << endl;
        return 1;
    }

    // Se define el pin que determina el fin de la lectura de datos
    int terminationPin = 17;
    pinMode(terminationPin, INPUT);

    // Se definen los parámetros para la lectura del puerto serial
    SerialStream arduino;
    arduino.Open("/dev/ttyACM0");

    if (!arduino.IsOpen())
    {
        cerr << "Failed to open the serial port." << endl;
        return 1;
    }

    arduino.SetBaudRate(BaudRate::BAUD_9600);
    arduino.SetCharacterSize(CharacterSize::CHAR_SIZE_8);
    arduino.SetStopBits(StopBits::STOP_BITS_1);
    arduino.SetParity(Parity::PARITY_NONE);
    arduino.SetFlowControl(FlowControl::FLOW_CONTROL_NONE);

    // Leer datos mientras el pin GPIO_17 se encuentre en estado ALTO
    vector<string> data;
    string value;
    delay(2000);	// Delay para compensar reinicio al activar comunicación serial
    while (digitalRead(terminationPin) == HIGH)
    {
        try
        {
            arduino >> value;
            data.push_back(value);
        }
        catch (const exception &e)
        {
            cerr << "Exception: " << e.what() << endl;
            return 1;
        }
    }

    // Guarda los datos recibidos en un archivo de texto
    ofstream outputFile("received_data.txt");
    if (outputFile.is_open())
    {
        for (const string &val : data)
        {
            outputFile << val << " ";
        }
        outputFile.close();
        cout << "Data saved to received_data.txt." << endl;
    }
    else
    {
        cerr << "Failed to open the output file." << endl;
    }

    // Cierra el puerto serial
    arduino.Close();

    return 0;
}
