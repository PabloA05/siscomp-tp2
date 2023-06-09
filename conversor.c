#include <stdlib.h>
#include <stdio.h>

extern float multiply(float, float);

#define ARGCANT 0
#define ARGTYPE 1
#define ARGINVA 2
#define RETERRO -1

void _printbanner(float num1)
{
    printf("###############################################\n");
    printf("----> Estamos en el wrapper conversor (C) <----\n");
    printf("Conversor: %f \n", num1);
    printf("###############################################\n");
}

void _printBannerError(int opt)
{
    printf("###############################################\n");
    printf("----> Estamos en el wrapper conversor (C) <----\n");
    switch (opt)
    {
    case ARGINVA:
        printf("El valor del argumento es invalida\n");
        break;
    default:
        break;
    }
    printf("###############################################\n");
}

float conversor(float number1, float number2)
{

    printf("\n--> Entrando a convesor con %.2f y %.2f\n", number1, number2);

    if (number1 < 0.0 || number2 < 0.0)
    {
        _printBannerError(ARGINVA);
        return RETERRO;
    }

    printf("--> call multiply.asm\n");
    float ret = multiply(number1, number2);
    printf("--> Valor recibido de multiply.asm : %.2f \n\n", ret);

    return ret;
}