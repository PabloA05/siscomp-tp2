AS		:= nasm
ASFLAGS := -f elf
CFLAGS	:= -m32
LDFLAGS := -m32
CC		:= gcc
CXX		:= g++
CXXFLAGS := -m32
TARGETS := conversor 
DEP := driver.o asm_io.o

.PHONY: clean

%.o: %.asm
	$(AS) $(ASFLAGS) $< 

all: $(TARGETS)
	
conversor: multiply.o conversor.c

clean :
	rm -f *.o $(TARGETS)
#nasm -f elf multiply.asm
#gcc -m32  multiply.c multiply.o   -o multiply 
