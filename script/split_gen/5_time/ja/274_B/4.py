def solve():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(W):
        cnt = 0
        for j in range(H):
            if C[j][i] == '#':
                cnt += 1
        print(cnt)
