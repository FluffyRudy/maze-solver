import random

import random

def create_maze(dim):
    maze = [[0 for _ in range(dim*2+1)] for _ in range(dim*2+1)]
    x, y = (0, 0)
    maze[2*x+1][2*y+1] = 1
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1][2*ny+1] == 0:
                maze[2*nx+1][2*ny+1] = 1
                maze[2*x+1+dx][2*y+1+dy] = 1
                stack.append((nx, ny))
                break
        else:
            stack.pop()
    maze[1][0] = 1
    maze[-2][-1] = 1

    maze_info = {
        "start": (1, 0),
        "end": (len(maze)-2, len(maze[0])-1),
        "maze": maze
    }

    return maze_info

def bfsTraversal(maze, srcPos, destPos):
    startRow, startCol = srcPos
    nodes = [srcPos]
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    path = [[None] * len(maze[0]) for _ in range(len(maze))]

    visited[startRow][startCol] = True

    while nodes:
        srcRow, srcCol = nodes.pop(0)

        if srcRow == destPos[0] and srcCol == destPos[1]:
            return constructPath(path, destPos)

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dirX, dirY in direction:
            newDirX = srcRow + dirX
            newDirY = srcCol + dirY

            if isValidPosition(maze, newDirX, newDirY) and not visited[newDirX][newDirY]:
                visited[newDirX][newDirY] = True
                nodes.append((newDirX, newDirY))
                path[newDirX][newDirY] = (srcRow, srcCol)
    return None

def constructPath(path, destPos):
    row, col = destPos
    result = []

    while path[row][col]:
        result.append((row, col))
        row, col = path[row][col]

    result.append((row, col))
    result.reverse()

    return result

def isValidPosition(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 1


maze_info = create_maze(30)
maze = maze_info["maze"]
start_position = maze_info["start"]
end_position   = maze_info["end"]
solution = bfsTraversal(maze, start_position, end_position)