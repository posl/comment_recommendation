def main():
    H,W = input().split()
    H = int(H)
    W = int(W)
    S = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x = i
                y = j
    print(abs(x - (H-1)) + abs(y - (W-1)))
main()
