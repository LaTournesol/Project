/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function print_heap
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

#include "mem.h"
#include "mem_impl.h"

// Print a formatted listing on file f showing the blocks on the free list.
// Each line of output describes one free block
// and begin with two hexadecimal number
void print_heap(FILE * f) {
    if (freeList != NULL) {
        int blockCount = 0;
        Header *currentPointer = freeList;
        fprintf(f, "%p 0x%x\n Block %u", currentPointer,
            (int)currentPointer->size, blockCount++);
        currentPointer = currentPointer->next;
        while (currentPointer != freeList) {
            fprintf(f, "%p 0x%x\n Block %u", currentPointer,
                (int)currentPointer->size, blockCount++);
            currentPointer = currentPointer->next;
        }
        fclose(f);
    }
}

