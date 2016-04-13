# Makefile for t9
# CSE 374 HW 05
# TianYang Jin

#default target
t9: t9.o trie.o
	gcc -Wall -std=c11 -g -o t9 t9.o trie.o

#individual sourse files
t9.o: t9.c
	gcc -Wall -std=c11 -g -c t9.c
trie.o: trie.c trie.h
	gcc -Wall -std=c11 -g -c trie.c

clean:
	rm -f *.o
