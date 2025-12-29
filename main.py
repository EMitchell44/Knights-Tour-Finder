from random import choice

width = 8
height = 8

# Each cell is a list containing x and y coordinates, a boolean indicating whether that cell has been
# visited, and a list of depths. If the current depth plus one is in that list, then access to the
# cell is forbidden.

board = [[[x, y, False, []] for y in range(width)] for x in range(height)]


def find_targets(coords):
    # Loops through moves clockwise and returns a list of moves that wouldn't run off the edge of the board.
    x = coords[0]
    y = coords[1]
    prospects = [
        [x + 1, y - 2],
        [x + 2, y - 1],
        [x + 2, y + 1],
        [x + 1, y + 2],
        [x - 1, y + 2],
        [x - 2, y + 1],
        [x - 2, y - 1],
        [x - 1, y - 2]
    ]
    return [t for t in prospects if t[0] in range(width) and t[1] in range(height)]


def delete(array, element):
    # Deletes a specified element from a list.
    if element in array:
        del array[array.index(element)]


def check_options(targets):
    cells = [board[t[0]][t[1]] for t in targets]
    return [cell for cell in cells if not cell[2]]


def check_unsolvable():
    # Returns true if there are any cells that are impossible to visit.
    # This is not strictly necessary to solve a knight's tour, but it can save
    # millions upon millions of guesses.
    for row in board:
        for cell in row:
            if not cell[2] and not check_options(find_targets(cell)):
                return True


depth = 1
starting_cell = board[0][0]
knight = starting_cell
trail = [knight]
count = 0
tour_found = False

while depth < width * height:
    targets = [board[t[0]][t[1]] for t in find_targets(knight)]
    options = [o for o in targets if not o[2] and depth + 1 not in o[3]]
    if options and not check_unsolvable():
        knight[2] = True
        # Move to a random target.
        knight = choice(options)
        trail.append(knight)
        depth += 1
    else:
        # Mark the current cell as unvisited.
        knight[2] = False
        # Mark this cell as forbidden from the previous depth.
        knight[3].append(depth)
        for t in targets:
            # Allow access to the targeted cell from the current depth.
            delete(t[3], depth + 1)
        # Go back to the last visited cell.
        del trail[-1]

        if len(trail) == 0:
            print("Starting at the given cell, it is impossible to find a Knight's Tour on a board of this size.")
            break
        knight = trail[-1]
        depth -= 1
    count += 1

    # Uncomment these lines to print out a statement every million iterations.
    # It's nice to have a little reminder that the program is doing something.
    # if not count % 1000000:
    #     print(f"{int(count / 1000000)} million iterations")

    # Uncomment these lines if you want to force stop the program after a certain number of iterations.
    # if count == 100000000:
    #     break

if len(trail) == width * height:
    tour_found = True

# I'm only adding the cell values for a standard 8x8 board.
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = ['8', '7', '6', '5', '4', '3', '2', '1']

is_found = [" ruled out ", " found "]
print(f"Tour{is_found[tour_found]}in {count} iterations.")

for i, cell in enumerate(trail):
    print(str(i + 1) + ": " + row[cell[0]] + col[cell[1]])
