TianYang Jin, Sheng Chen   
Instructor: S. Tanimoto.   
The problem being formulated is Sliding Blocks of 10 pieces. The pieces consists of four types, 1x1, 2x1, 1x2, and 2x2.   
Here is a rough drawing of the Initial state and a representation of the goal state:    
1 2 2 7  
1 2 2 8                            
3 5 5 9               
3 4 6 10                          
0 4 6 0      
↓   
. . . .   
. . . .  
. . . .  
. 2 2 .  
. 2 2 .  
The goal of this game is to get the 2x2 block to the shown position, all other pieces' positions don't matter.   
But the piece can only move to an empty space (represented by 0) and it can only move if the space can fit.   
In this program, each state of the board is represented by a simple GUI interface produced using the package Tkinter.   

CSE 415, Spring 2016, University of Washington


Sample test command:
       python3 AStar.py SlidingBlocksProblem h_combined_min testInitialState.py 

       It took the ASar search algorithm about 160s to solve the problem using the 'combined_min' heuristic function, and it displays the solution path at then end using the same simple GUI interface.