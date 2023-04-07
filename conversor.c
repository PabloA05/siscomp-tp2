#include <stdlib.h>
#include <stdio.h>

#define ARGCANT 0
#define ARGTYPE 1
#define ARGINVA 2

void _printbanner (float num1, float num2){
    printf ("###############################################\n");
    printf ("----> Estamos en el wrapper conversor (C) <----\n");
    printf ("Conversor: %f %f\n", num1, num2);
    printf ("###############################################\n");
}


void _printBannerError (int opt){
    printf ("###############################################\n");
    printf ("----> Estamos en el wrapper conversor (C) <----\n");
    switch (opt)
    {
    case ARGCANT:
        printf ("La cantidad de argumentos es invalida\n");
        break;
    case ARGINVA:
        printf ("El valor del argumento es invalida\n");
        break;
    default:
        break;
    }
    printf ("###############################################\n");

}

float conversor(float number1, float number2) {

    if (number1 < 0.0 || number2 < 0.0)
    {
        _printBannerError (ARGINVA);
        return -1;
    }
    
    _printbanner (number1, number2);
    return 1000;
}
