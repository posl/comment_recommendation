def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(H):
        cnt = 0
        for j in range(W):
            if C[i][j] == '#':
                cnt += 1
        print(cnt)
