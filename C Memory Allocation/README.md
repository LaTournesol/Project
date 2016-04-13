CSE 374 HW6

1. TianYang Jin: freemem.c bench.c check_heap.c get_mem_stats.c makefile
   kanghui Liu:  getmen.c bench.c print_heap.c mem.h mem_impl.h


2. We used the circular linked list as the data structure.
   Getmem returns the pointer to the address of the block user required.
   If the block is too big, it will be splited into two with reasonable size
   Freeblock will be merged together if they are adjacent to each other.

3. We did the first extra credit. it made our linked list to a circular linked list
   With circular linked list, fragments of free space at the beginning of the list will be reduced.

4. When runnning with the default parameter,
   it gives exactly 10 reports during every run time, and it reports the following infomation: Total CPU time used,
               Total memory storage accolated,
	       Total number of blocks on the free list
	   and Average number of bytes in the free storage blocks
   on average, the total CPU time used for each report is around 0.002s
           and the average number of bytes in the free storage blocks is about 1000~1500.

5. During our implementation of the getmem and freemem functions, we had the C textbook as reference since there's a sample function and it really helped us understanding what we were suppose to implement. 
   


