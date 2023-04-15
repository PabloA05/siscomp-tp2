AS		:= nasm
ASFLAGS := -f elf64 
CFLAGS	:= -m64
LDFLAGS := -m64
CC		:= gcc
CXX		:= g++
CXXFLAGS := -m64
TARGETS := multiply 
DEP := driver.o asm_io.o

.PHONY: clean

%.o: %.asm
	$(AS) $(ASFLAGS) $< 

all: $(TARGETS)
	
multiply: multiply.o main.c


clean :
	rm -f *.o $(TARGETS)
#  5561  nasm -f elf64 -o multiply.o multiply.asm
#  5562  gcc -c -m64 -Wall -Wextra -pedantic -std=c11 -o main.o main.c
#  5563  gcc -m64 -o mult main.o multiply.o