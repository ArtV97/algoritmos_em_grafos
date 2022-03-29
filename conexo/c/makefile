TARGET := conexo
COMPILER := gcc



$(TARGET): util.o simple_graph.o
	$(COMPILER) $(TARGET).c -o bin util.o simple_graph.o

util.o: util.c
	gcc -c util.c

simple_graph.o: simple_graph.c
	gcc -c simple_graph.c

clean:
	rm *o