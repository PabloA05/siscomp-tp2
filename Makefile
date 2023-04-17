CC:=gcc
AS:=nasm
CFLAGS:=-c -Wall -Werror
ASFLAGS:=-f elf64
LIBFLAGS:=-shared -o libconversor.so

SRCS:=conversor.c multiply.asm
OBJS:=conversor.o multiply.o

all: libconversor.so

libconversor.so: $(OBJS)
	$(CC) $(LIBFLAGS) $(OBJS)

conversor.o: conversor.c
	$(CC) $(CFLAGS) conversor.c

multiply.o: multiply.asm
	$(AS) $(ASFLAGS) -o multiply.o multiply.asm

clean:
	rm -f *.o libconversor.so


#  5651* nasm -f elf64 multiply.asm
#  5652* gcc -c conversor.c
#  5653* gcc -shared -o libconversor.so conversor.o multiply.o