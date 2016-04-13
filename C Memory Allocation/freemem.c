/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function freemem
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

#include "mem.h"
#include "mem_impl.h"

// Return the block of storage at location p to
// the pool of available free storage.
void freemem(void* p) {
  // return silently if p is null
  if (p == NULL) {
    return;
  }
  Header *hp, *ptr;
  hp = (Header*) p - 1;           // Pointer to the header of the given block
  ptr = freeList;                 // Pointer to loop through the freelist
  // check_heap();
  // Search for a place in the freelist to place the given block
  // Break out the while loop when found one
  // Break out the method when no place is available
  while (!(hp > ptr && hp < ptr->next)) {
    if (ptr == hp) {
      return;
    }
    if (ptr >= ptr->next && (hp > ptr || hp < ptr->next)) {
      break;
    }
    ptr = ptr->next;
  }
  // If there is an adjacent free block on the right
  // combine them
  if (hp + hp->size == ptr->next) {
    hp->size += ptr->next->size;
    hp->next = ptr->next->next;
  } else {
    hp->next = ptr->next;
  }

  // If there is an adjacent free block on the left
  // combine them
  if (ptr + ptr->size == hp) {
    ptr->size += hp->size;
    ptr->next = hp->next;
  } else {
    ptr->next = hp;
  }
  freeList = ptr;
}
