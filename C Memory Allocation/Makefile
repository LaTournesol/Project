# Makefile for mem
# CSE 374 HW 06
# TianYang Jin, KangHui Liu

# default target
bench: bench.o getmem.o freemem.o get_mem_stats.o print_heap.o check_heap.o
	gcc -Wall -std=c11 -g -o bench bench.o check_heap.o getmem.o freemem.o get_mem_stats.o print_heap.o

# individual sourse files
bench.o: bench.c mem.h
	gcc -Wall -std=c11 -g -c bench.c

check_heap.o: check_heap.c mem.h mem_impl.h
	gcc -Wall -std=c11 -g -c check_heap.c

getmem.o: getmem.c mem.h mem_impl.h
	gcc -Wall -std=c11 -g -c getmem.c

freemem.o: freemem.c mem.h mem_impl.h
	gcc -Wall -std=c11 -g -c freemem.c

get_mem_stats.o: get_mem_stats.c mem.h mem_impl.h
	gcc -Wall -std=c11 -g -c get_mem_stats.c

print_heap.o: print_heap.c mem.h mem_impl.h
	gcc -Wall -std=c11 -g -c print_heap.c

# run the bench with default program
test:
	make bench
	./bench

# create an archive containing the source files
dist:
	make clean
	git log > git.log
	tar cvf hw6.tar *
	rm git.log

clean:
	rm -f *.o bench *~ *tar *.log \
