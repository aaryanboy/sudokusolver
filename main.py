grid=[    [0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]  ]

def checkvalid(problem, row, col, number):
    for i in range(9):

        # rows check
        if number == problem[row][i]:
            return False
        

    for j in range(9):
        # column check
        if number == problem[j][col]:
            return False

    # cube check
    i = (row // 3) * 3
    j = (col // 3) * 3

    for a in range(3):
        for b in range(3):
            if problem[i + a][j + b] == number:
                return False
    return True


#does this code works
def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None



def lopp(grid):
    row, col = find_empty_location(grid)

    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
# i domt think so need to fix it 
    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if checkvalid(grid, row, col, num):
            # If the move is valid, assign the number to the empty cell
            grid[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if lopp(grid):
                return True

            # If the current assignment does not lead to a solution, backtrack
            grid[row][col] = 0

    # No solution found for the current configuration
    return False
need to remember pytho. agani dyam its tuff

lopp(grid)


print(grid)


