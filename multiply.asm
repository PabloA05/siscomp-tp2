;
; file: multiply.asm

global multiply

segment .text

%define d1   [ebp+8]
%define d2   [ebp+16]

multiply:
        enter   0, 0

        fld     qword d2
        fld     qword d1            ; ST0 = d1, ST1 = d2
        fmul          

exit:
        leave
        ret