# 
# Author : Rumman
# Project Name: Successor OR Expand function
# Problem: predicting moves for Puzzle/Games
# github: /MRummanHasan

'''
# Successor OR Expand function for Sudoku Puzzle 
                       j   j   j
  | 2, 1, 3|      i | 0,0 0,1 0,2 |
  | 4, 5, _|  ==> i | 1,0 1,1 1,2 |
  | 7, 8, 6|      i | 2,0 2,1 2,2 |  

#empty tile can be represented by -1
'''
# Function Algo
'''
function successorFunction(currentState){

# STEP 1:
index = findEmpty tile

# STEP 2:
find allmoves()
    (i+1,j) or (i,j+1) or (i-1,j) or (i,j-1)
      2 ,2      1, 3        0 ,2      1, 1 #index Number

# STEP 3:
find invalidMoves()
    if i <= 2 or j >=2
        OK
    else
        invalid

remainingMoves = (i+1,j) and (i-1,j) and (i,j-1)
                   2 ,2        0 ,2       1, 1  #index Number
              
#STEP 4:
for all remainingMoves;
    swap((i,j),1)
}

'''