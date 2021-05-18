#include <Keypad.h>
#include <Servo.h>

//empieza codigo

int ledGreen = 3;
int ledRed = 2;

const byte filas = 4; // 4 rows
const byte columnas = 4; // 3 columns

byte pinsfilas[filas] = { 13,12,11,10 };
byte pincolumnas[columnas] = { 7,6,5,4 };

char teclas[filas][columnas] = {
{'1','2','3','A'},
{'4','5','6','B'},
{'7','8','9','C'},
{'*','0','#','D'}
};

Keypad teclado = Keypad( makeKeymap(teclas), pinsfilas, pincolumnas, filas, columnas );
Servo ServoMotor;
char tecla;
char contrasena[5];
char contrasenareal[5] = "16A0";
byte index = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledRed, OUTPUT);
  ServoMotor.attach(A0);
}

void loop() 
{
  // put your main code here, to run repeatedly:
  tecla = teclado.getKey();
  if (tecla != NO_KEY)
  {
    if (tecla == '*' || tecla == '#')
     { 
       digitalWrite(ledRed,HIGH);
       digitalWrite(ledGreen,LOW);
       ServoMotor.write(0);
       Serial.print(tecla);
     }
     else
     {
       Serial.print(tecla);
       contrasena[index] = tecla;
       index++;
     }
  }

  if (index == 4)
  {
    byte check = 0;
      for(int i=0;i<4; i++)
      {
        Serial.print(contrasena[i]);
        if (contrasena[i] == contrasenareal[i])
        {
          check++;
        }
      }

        if (check == 4)
         {
           digitalWrite(ledGreen,HIGH);
           digitalWrite(ledRed,LOW);
           ServoMotor.write(90);
           Serial.println("Abiert");
         }
        else
         {
           digitalWrite(ledGreen,LOW);
           digitalWrite(ledRed,HIGH);
           ServoMotor.write(0);
           Serial.println("Contrasena incorrecta");
         }
        index = 0;
    }
}
  
