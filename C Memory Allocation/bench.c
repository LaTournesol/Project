/*
 * CSE 374 HW 06
 * TianYang Jin, KangHui Liu
 * Implementation of function main function
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <inttypes.h>
#include <time.h>

#include "mem.h"

int main(int argc, char** argv) {
  if (argc > 6) {
    fprintf(stderr, "Need no more than 6 parameters.");
    return 1;
  }
  //  Initialize all the variables
  uintptr_t total_size = 0;
  uintptr_t free_total = 0;
  uintptr_t total_num_of_blocks = 0;
  uintptr_t ave_num_of_bytes = 0;

  clock_t start_t, terminate_t;
  double total_t;

  //  Initialize the input parameter array
  //  Put in defalut value if needed
  int inputs[6];
  int defaults[6] = {10000, 50, 10, 200, 20000, (int)time(NULL)};
  for (int i = 1; i < argc; i++) {
    inputs[i-1] = atoi(argv[i]);
  }
  for (int j = 7-argc; j > 0; j--) {
    inputs[6-j] = defaults[6-j];
  }

  int ntrials = inputs[0];
  int pctget = inputs[1];
  int pctlarge = inputs[2];
  int small_limit = inputs[3];
  int large_limit = inputs[4];
  int random_seed = inputs[5];

  void * testVoid;
  void **test_memblocks = malloc(sizeof(testVoid) * ntrials);
  int test_block_size = 0;
  int report_period = (int) (0.1 * ntrials);
  int report_tracker = report_period;
  start_t = clock();
  srand(random_seed);
  for (int i = 0; i < ntrials; i++) {
    bool isGet = true;                // false if it's to free
    // create a random number between 0 and 100
    int getOrFree = rand() % 100;
    if (getOrFree > pctget) {
      isGet = false;
    }
    if (isGet) {                      // calling getmem
      bool isSmall = true;            // faluse if it's a large block
      int smallOrLarge = rand() % 100;
      if (smallOrLarge < pctlarge) {
        isSmall = false;
      }
      int blockSize;
      if (isSmall) {
        blockSize = rand() % small_limit + 1;
      } else {
        blockSize = rand() % (large_limit - small_limit) + small_limit;
      }
      test_memblocks[test_block_size] = getmem((uintptr_t) blockSize);
      blockSize++;
    } else {  //  calling freemem
      if (test_block_size > 0) {     // if there are blocks being allocated
        int rIndex = rand() % test_block_size;
        freemem(test_memblocks[rIndex]);
        test_memblocks[rIndex] = test_memblocks[test_block_size];
        test_block_size--;
      }
    }

    if (i == report_tracker - 1) {
      printf("Report No.%d\n", i/(ntrials/10) + 1);
      get_mem_stats(&total_size, &free_total, &total_num_of_blocks);
      terminate_t = clock();
      total_t = (double) (terminate_t - start_t) / CLOCKS_PER_SEC;
      if (total_num_of_blocks == 0) {
        ave_num_of_bytes = 0;
      } else {
        ave_num_of_bytes = free_total / total_num_of_blocks;
      }
      printf("Total CPU time used:                                %.8f\n",
             total_t);
      printf("Total memory storage accolated:                     %lu\n",
             total_size);
      printf("Total number of blocks on the free list:            %lu\n",
             total_num_of_blocks);
      printf("Average number of bytes in the free storage blocks: %lu\n\n",
             ave_num_of_bytes);
      report_tracker += report_period;
    }
  }
  free(test_memblocks);
  return 0;
}
