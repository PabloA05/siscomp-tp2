#include <stdio.h>
#include "cdecl.h"

float PRE_CDECL multiply( float, float ) POST_CDECL;

int main()
{
  float d1 = 2.2, d2=1.3;
  printf("Result of %f * %f is %f\n", d1, d2, multiply(d1,d2));
  return 0;
}