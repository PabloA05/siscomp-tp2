; NASM : Netwide
; MASM : microsoft
; TASM : Borland

; --> Instrucciones <--
; MOV dest, src
; ADD eax, 4 -> eax = aex + 4
; ADD al, ah -> al = al + ah
; INC ecx
; DEC dl
; simbolo EQU valor
; %define <name> <val>

%include "asm_io.inc"
segment .data
;
; los datos iniciados se colocan en el segmento de
; datos ac ́a
;
prompt1 db "---> Entrando a asm", 0
prompt2 db "---> Saliendo de asm", 0

segment .bss
;
; Datos no iniciados se colocan en el segmento bss
;
segment .text
    global _asm_main
_asm_main:
    enter 0,0 ; rutina de
    pusha

    mov eax, prompt1
    call print_string

    mov eax, prompt2
    call print_string
;
; El c ́odigo est ́a colocado en el segmento de texto. No modifique el
; c ́odigo antes o despu ́es de este comentario
;
    popa    
    mov eax, 10 ; retornar a C
    leave
    ret