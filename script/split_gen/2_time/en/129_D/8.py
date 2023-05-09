def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    
    # up
    up = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0:
                if S[i][j] == '.':
                    up[i][j] = 1
                else:
                    up[i][j] = 0
            else:
                if S[i][j] == '.':
                    up[i][j] = up[i-1][j] + 1
                else:
                    up[i][j] = 0
    #print(up)
    
    # down
    down = [[0] * W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W):
            if i == H-1:
                if S[i][j] == '.':
                    down[i][j] = 1
                else:
                    down[i][j] = 0
            else:
                if S[i][j] == '.':
                    down[i][j] = down[i+1][j] + 1
                else:
                    down[i][j] = 0
    #print(down)
    
    # left
    left = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if j == 0:
                if S[i][j] == '.':
                    left[i][j] = 1
                else:
                    left[i][j] = 0
            else:
                if S[i][j] == '.':
                    left[i][j] = left[i][j-1] + 1
                else:
                    left[i][j] = 0
    #print(left)
    
    # right
    right = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W-1, -1, -1):
            if j == W-1:
                if S[i][j] == '.':
                    right[i][j] = 1
                else:
                    right[i][j] = 0
            else:
                if
