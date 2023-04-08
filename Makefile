AS		:= nasm
ASFLAGS := -f elf
CFLAGS	:= -m32
LDFLAGS := -m32
CC		:= gcc
CXX		:= g++
CXXFLAGS := -m32
TARGETS := multiply 
DEP := driver.o asm_io.o

.PHONY: clean

%.o: %.asm
	$(AS) $(ASFLAGS) $< 

all: $(TARGETS)
	
multiply: multiply.o main.c


clean :
	rm -f *.o $(TARGETS)
#nasm -f elf multiply.asm
#gcc -m32  multiply.c multiply.o   -o multiply 
