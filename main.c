#include <stdio.h>
#include "cdecl.h"

double PRE_CDECL multiply( double, double ) POST_CDECL;

int main()
{
  double d1, d2;

  printf("Enter two floats: ");
  scanf("%lf %lf", &d1, &d2);

  printf("Result of %g * %g is %g\n", d1, d2, multiply(d1,d2));
  return 0;
}