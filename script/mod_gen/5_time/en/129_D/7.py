def main():
    H, W = [int(x) for x in input().split()]
    S = []
    for i in range(H):
        S.append(input())
    #print(H,W,S)
    # 1. Find the number of squares lighted by the lamp placed at each square
    # 2. Find the maximum number of squares lighted by the lamp
    # 1. Find the number of squares lighted by the lamp placed at each square
    # 1.1. Find the number of squares lighted by the lamp placed at each square in the up direction
    up = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                up[i][j] = 0
            elif i == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i-1][j] + 1
    #print(up)
    # 1.2. Find the number of squares lighted by the lamp placed at each square in the down direction
    down = [[0 for i in range(W)] for j in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == '#':
                down[i][j] = 0
            elif i == H-1:
                down[i][j] = 1
            else:
                down[i][j] = down[i+1][j] + 1
    #print(down)
    # 1.3. Find the number of squares lighted by the lamp placed at each square in the left direction
    left = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                left[i][j] = 0
            elif j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1
    #print(left)
    # 1.4. Find the number of squares lighted by the lamp placed at each square in the right direction
    right = [[0 for i

if __name__ == '__main__':
    main()