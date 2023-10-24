int i = 0;

void setup() {
  // Inicializa la comunicación serial a 9600 baudios
  Serial.begin(9600);
  pinMode(7,OUTPUT);  // Declara pin 7 como salida
}

void loop() {
  if( i < 32000){       // Condición de contador para generar los 32.000 datos
  digitalWrite(7,HIGH); // Mantener pin 7 en ALTO mientras se envían datos
  int randomNumber = random(1024);
  Serial.println(randomNumber);   // Imprimir por serial
  i=i+1;
  }
  else
  digitalWrite(7,LOW);  // Una vez terminado el ciclo bajar pin 7
}

