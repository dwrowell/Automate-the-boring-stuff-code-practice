#example code from chaper 4 of ATtBS

#Desired Output:
    #..OO.OO..
    #.OOOOOOO.
    #.OOOOOOO.
    #..OOOOO..
    #...OOO...
    #....O....

grid = [['.', '.', '.', '.', '.', '.'], #starting grid
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#need code to automatically rotate this by
#this reddit thread helped explain it https://www.reddit.com/r/learnpython/comments/5xq28k/need_explanation_for_atbs_chapter_4/ 

def functionGrid(grid):
    for y in (range (6)):
        for x in (range(9)):
            print (grid[x][y], end='')
        print()
     
functionGrid(grid)


