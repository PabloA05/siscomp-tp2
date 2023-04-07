#include <stdlib.h>
#include <stdio.h>

#define ARGCANT 0
#define ARGTYPE 1
#define ARGINVA 2
#define RETERRO -1

void _printbanner (float num1){
    printf ("###############################################\n");
    printf ("----> Estamos en el wrapper conversor (C) <----\n");
    printf ("Conversor: %f \n", num1);
    printf ("###############################################\n");
}

void _printBannerError (int opt){
    printf ("###############################################\n");
    printf ("----> Estamos en el wrapper conversor (C) <----\n");
    switch (opt)
    {
    case ARGINVA:
        printf ("El valor del argumento es invalida\n");
        break;
    default:
        break;
    }
    printf ("###############################################\n");
}

float conversor(float number1, float number2) {

    printf ("--> Entrando a convesor ubicado en .c\n");
    
    // se comprueba los valores recibidos
    if (number1 < 0.0 || number2 < 0.0)
    {
        _printBannerError (ARGINVA);
        return RETERRO;
    }
    
    // se llama al codigo asm    
    printf ("--> call <file>.asm\n");
    float ret = 10.4; // = <file>.asm
    printf ("--> Valor recibido de <file>.asm : %f \n", ret);

    return ret;
}
