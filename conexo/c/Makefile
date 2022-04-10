TARGET := conexo
COMPILER := gcc



$(TARGET): util.o simple_graph.o
	-mkdir bin
	$(COMPILER) $(TARGET).c -o bin/$(TARGET) util.o simple_graph.o

util.o: util.c
	gcc -c util.c

simple_graph.o: simple_graph.c
	gcc -c simple_graph.c

clean:
	rm -r bin
	rm *o