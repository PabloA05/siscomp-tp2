AS		:= nasm
ASFLAGS := -f elf64 
CFLAGS	:= -m64
LDFLAGS := -m64
CC		:= gcc
CXX		:= g++
CXXFLAGS := -m64
TARGETS := conversor 
DEP := driver.o asm_io.o

.PHONY: clean

%.o: %.asm
	$(AS) $(ASFLAGS) $< 

all: $(TARGETS)
	
conversor: multiply.o conversor.c

clean :
	rm -f *.o $(TARGETS)
#    nasm -f elf64 -o multiply.o multiply.asm
#    gcc -c -m64 -Wall -Wextra -pedantic -std=c11 -o main.o main.c
#    gcc -m64 -o mult main.o multiply.o
