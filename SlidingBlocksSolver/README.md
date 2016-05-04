'''AStar.py
TianYang Jin, Sheng Chen
The problem being formulated is Sliding Blocks of 10 pieces. The pieces consists of four types, 1x1, 2x1, 1x2, and 2x2.
Here is a rough drawing of the Initial state and a representation of the goal state: <br />
1 2 2 7                            . . . .<br />
1 2 2 8                            . . . .<br />
3 5 5 9            ------->        . . . .<br />
3 4 6 10                           . 2 2 .<br />
0 4 6 0                            . 2 2 .<br />
The goal of this game is to get the 2x2 block to the shown position, all other pieces' positions don't matter.
But the piece can only move to an empty space (represented by 0) and it can only move if the space can fit.
In this program, each state of the board is represented by a simple GUI interface produced using the package Tkinter.
It took the ASar search algorithm about 160s to solve the problem using the 'combined_min' heuristic function, and it
displays the solution path at then end using the same simple GUI interface.
CSE 415, Spring 2016, University of Washington
Instructor: S. Tanimoto.
'''