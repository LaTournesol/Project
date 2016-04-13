/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function get_mem_stats
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

#include "mem.h"
#include "mem_impl.h"

// Store statistics about the current state of the memory manager in the three
// integer variables whose addresses are given as arguments.
void get_mem_stats(uintptr_t* total_size, uintptr_t* total_free,
                   uintptr_t* n_free_blocks) {
  *total_size = totalMalloc;
  *total_free = 0;
  *n_free_blocks = 0;

  if (freeList != NULL) {
     Header* curr = freeList;
    if (curr->size != 0) {
      *total_free = curr->size;
      *n_free_blocks = 1;
    }
    curr = curr->next;
    while (curr != freeList) {
      if (curr->size != 0) {
               *total_free += curr->size;
               *n_free_blocks += 1;
      }
      curr = curr->next;
    }
  }
}
