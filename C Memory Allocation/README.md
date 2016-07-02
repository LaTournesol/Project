CSE 374 HW6

1. Autor: TianYang Jin, Kanghui Liu

2. We used the circular linked list as the data structure.
   Getmem returns the pointer to the address of the block user required.
   If the block is too big, it will be splited into two with reasonable size
   Freeblock will be merged together if they are adjacent to each other.

3. When runnning with the default parameter,
   it gives exactly 10 reports during every run time, and it reports the following infomation: 
      	       Total CPU time used,
               Total memory storage accolated,
	       Total number of blocks on the free list
	   and Average number of bytes in the free storage blocks
   on average, the total CPU time used for each report is around 0.002s
           and the average number of bytes in the free storage blocks is about 1000~1500.

4. Sample test command:
   	  make
   	  ./bench
   


