ARCH := $(shell uname -m)

ifeq ($(ARCH), aarch64)
	CC := aarch64-linux-gnu-gcc
	AS := aarch64-linux-gnu-as
	ASFLAGS := -march=armv8-a
	MULTIPLY_ASM := multiply_aarch64.asm
else
	CC := gcc
	AS := nasm
	ASFLAGS := -f elf64
	MULTIPLY_ASM := multiply_x86_64.asm
endif
CFLAGS:=-c -Wall -Werror
LIBFLAGS:=-shared -o libconversor.so

SRCS:=conversor.c $(MULTIPLY_ASM)
OBJS:=conversor.o multiply.o

all: libconversor.so

libconversor.so: $(OBJS)
	$(CC) $(LIBFLAGS) $(OBJS)

conversor.o: conversor.c
	$(CC) $(CFLAGS) conversor.c

multiply.o: $(MULTIPLY_ASM)
	$(AS) $(ASFLAGS) -o multiply.o $(MULTIPLY_ASM)

install:
	python3 -m pip install -r requirements.txt

clean:
	rm -f *.o libconversor.so


#  5651* nasm -f elf64 multiply.asm
#  5652* gcc -c conversor.c
#  5653* gcc -shared -o libconversor.so conversor.o multiply.o

