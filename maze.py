maze = [
    [1]*30,
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0]*14 + [0],
    [0] + [1]*28 + [0],
    [0] + [1, 0, 0, 1, 1, 0]*5 + [0],
    [1]*30
]

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

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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


start_position = (15, 1)
end_position   = (len(maze)-1, len(maze[0])-1)
solution = bfsTraversal(maze, start_position, end_position)