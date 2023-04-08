#include <stdlib.h>
#include <stdio.h>

#define ARGCANT 0
#define ARGTYPE 1
#define ARGINVA 2
#define RETERRO -1

int asm_main() __attribute__ ((cdecl));

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
    
    if (number1 < 0.0 || number2 < 0.0)
    {
        _printBannerError (ARGINVA);
        return RETERRO;
    }
     
    printf ("--> call <file>.asm\n");
    int ret = asm_main(); 
    printf ("--> Valor recibido de <file>.asm : %d \n", ret);

    return 10.4;
}
