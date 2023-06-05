def dfs(start, goal, maze, visited, count):
    if start[0] == goal[0] and start[1] == goal[1]:
        return count
    else:
        visited[start[0]][start[1]] = 1
        if start[0] > 0 and maze[start[0]-1][start[1]] == '.' and visited[start[0]-1][start[1]] == 0:
            count = dfs([start[0]-1, start[1]], goal, maze, visited, count+1)
        if start[1] > 0 and maze[start[0]][start[1]-1] == '.' and visited[start[0]][start[1]-1] == 0:
            count = dfs([start[0], start[1]-1], goal, maze, visited, count+1)
        if start[0] < len(maze)-1 and maze[start[0]+1][start[1]] == '.' and visited[start[0]+1][start[1]] == 0:
            count = dfs([start[0]+1, start[1]], goal, maze, visited, count+1)
        if start[1] < len(maze[0])-1 and maze[start[0]][start[1]+1] == '.' and visited[start[0]][start[1]+1] == 0:
            count = dfs([start[0], start[1]+1], goal, maze, visited, count+1)
    return count
