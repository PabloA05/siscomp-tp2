#include <stdio.h>
//#include "cdecl.h"

extern float  multiply( float, float ) ;

int main()
{
  float d1 = 2.2, d2=1.3;
  printf("Result of %f * %f is %f\n", d1, d2, multiply(d1,d2));
  return 0;
}