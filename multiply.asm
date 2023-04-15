; file: multiply.asm

global multiply
segment .text

multiply:
        mulss xmm0,xmm1
        ret