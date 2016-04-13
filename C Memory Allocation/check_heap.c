/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function check_heap()
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>
#include <assert.h>

#include "mem.h"
#include "mem_impl.h"


// Check for possible problems with the free list data structure.
void check_heap() {
  Header* currPtr = freeList;
  while (currPtr->next != freeList) {
    if (currPtr->next != NULL) {
      assert((uintptr_t) currPtr + currPtr->size < (uintptr_t) currPtr->next);
      assert((uintptr_t) currPtr < (uintptr_t) currPtr->next);
      printf("curr size: %d", (int)currPtr->size);
      assert((int) currPtr->size > MIN_BLOCK_SIZE);
    }
    currPtr = currPtr->next;
  }
}
