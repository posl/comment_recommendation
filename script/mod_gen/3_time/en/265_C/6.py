def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    visited = [[False for j in range(w)] for i in range(h)]
    i = 0
    j = 0
    while True:
        visited[i][j] = True
        if grid[i][j] == "U":
            i -= 1
        elif grid[i][j] == "D":
            i += 1
        elif grid[i][j] == "L":
            j -= 1
        elif grid[i][j] == "R":
            j += 1
        else:
            print("Error")
            return
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            return
        if visited[i][j]:
            print(-1)
            return
main()

if __name__ == '__main__':
    main()