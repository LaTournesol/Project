/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function getmem
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdbool.h>

#include "mem.h"
#include "mem_impl.h"

Header* freeList = NULL;
Header firstBlock;
uintptr_t totalMalloc = 0;


//  return a new pointer to a new block of storage with at least size bytes of
//  memory.
//  the pointer to the returned block is aligned on an 16-byte boundary.
//  the block may be larger than the size requested.
//  pre: size > 0 if size is not positive, return NULL>
void* getmem(uintptr_t size) {
    Header *currentPtr;
    Header *prevPtr;
    uintptr_t mallocSize;
    uintptr_t alignRequireSize;

    //  return NULL if size is not positive
    if (size <= 0) {
        return NULL;
    }

    //  Round up to 16-byte boundary
    alignRequireSize = (size + (ALIGNMENT - 1)) & -ALIGNMENT;
    prevPtr = freeList;

    //  if there is no freeList at first, initialize a freelist  with 0 size
    if (prevPtr == NULL) {
        firstBlock.next = &firstBlock;
        freeList = &firstBlock;
        prevPtr = &firstBlock;
        firstBlock.size = 0;
    }

    currentPtr = prevPtr->next;

    //  find the suitable size block return the pointer.
    while (true) {
        if (currentPtr->size >= alignRequireSize) {
            // if there is no need to split the block into two blocks
            if (currentPtr->size <= alignRequireSize + MIN_BLOCK_SIZE) {
                // remove the block from the free list
                prevPtr->next = currentPtr->next;
            } else {
                // change the block size
                currentPtr->size = currentPtr->size - alignRequireSize;
                // move the pointer to the next block
                currentPtr = currentPtr + (currentPtr->size / ALIGNMENT);
                currentPtr->size = alignRequireSize;
            }
            freeList = prevPtr;
            return (void*)(currentPtr + 1);
        }

        // if there is no suitabe block find,
        // when reach the end of the freelist.
        // grow the freelist
        if (currentPtr == freeList) {
            mallocSize = alignRequireSize;
            if (alignRequireSize < MIN_MALLOC_SIZE) {
                mallocSize = MIN_MALLOC_SIZE;
            }
            currentPtr = (Header*) malloc(mallocSize);
            currentPtr->size = mallocSize;
            // send the currentPtr to freemem to get the newlist freelist
            freemem((void*)(currentPtr + 1));
            currentPtr = freeList;
            totalMalloc += mallocSize;
        }
        prevPtr = currentPtr;
        currentPtr = currentPtr->next;
    }
}
