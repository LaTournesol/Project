/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * header file with declarations of internal implementation details
 */

#ifndef MEM_IMPL_H
#define MEM_IMPL_H

#include <inttypes.h>
#include <stdlib.h>

#define ALIGNMENT 16
#define MIN_BLOCK_SIZE 32
#define MIN_MALLOC_SIZE 8192

// Defines the structure of the header of a freeNode
typedef struct Header_ {
  uintptr_t size;
  struct Header_* next;
} Header;

extern  Header firstBlock;     //  the first Header Block
extern  Header* freeList;      //  pointer to the freeList
extern uintptr_t totalMalloc;  //  record the total malloced block size.

#endif
