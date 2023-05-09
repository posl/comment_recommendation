def main():
    #input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #count
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    #output
    print(count)
