# Knights-Tour-Finder
This is a little Python script I threw together (which I'm sure is in dire need of refactoring) that can find a random Knight's tour on a chess board of arbitrary size, or inform the user that such a tour is impossible. I wanted to see if I could devise an algorithm for solving this problem with no help from online tutorials; I succeeded. As always for me, absolutely no AI was used to write any of this code.

## Abstract Overview of the Algorithm

As the knight progresses through a tour, it accumulates depth and save each cell it's visited to a list. The tour is completed if the depth is equal to the board's width times it's height.

Each cell on the chess board is represented by a list of four items: x coordinates, y coordinates, a boolean representing whether that cell has been visited, and a list of depths. For instance, a cell with the values 

```[5, 5, False, [40, 47, 55]]``` 

tells the knight "I have not been visited, but don't visit me if you're on move 39, 46, or 54."

The knight is first given a list of cells to which it can move without running off the edge of the board. These cells are further whittled down to which ones have not been visited and do not contain any forbidden depth value. If it cannot find such a cell, then it will remove it's current depth plus one from the depth list of all targeted cells, add its current depth to it's current cells depth list, mark its current cell as unvisited, delete its current cell from its list of visited cells, and return to the last visited cell. This is for the knight to remember which cells are dead ends from its current sequence of moves. If it tries to backtrace past its starting square, then then the program will break the main loop and inform the user that a Knight's Tour is impossible with the given parameters (because it's exhausted all possible paths).

As an optimization, the program also marks the current cell as a dead end (i.e. adds its current depth to its current cell's depth list and backtraces) if it finds any cells on the board that are impossible to visit. This adds quite a bit of computation to each step, but it saves untold millions of iterations. I first thought to implement this when I made a graphical program (just a grid where squares could be numbered) for testing this algorithm, and figured it didn't make any sense to keep testing and backtracing when there were obviously cells that could never be visited without further backtracing.

## Usage

Since this program can take a while to execute on a standard 8x8 board (maybe about twenty minutes to half an hour on a PC), there are a few lines that can be uncommented to give periodic reminders that the program is doing something, along with lines that can be uncommented to stop the program after a given number of moves. All relevant variables are changed from within the code itself. At some point, I ought to refactor main.py to make it neater and more user friendly, and maybe even make some attempt to implement Warnsdorff's rule.

## Further Reading

https://en.wikipedia.org/wiki/Knight%27s_tour
