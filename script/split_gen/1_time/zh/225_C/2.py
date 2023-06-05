def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    B = sorted(B)
    for i in range(N):
        for j in range(M):
            if B[i][j] != (i * 7 + j + 1):
                print("No")
                return
    print("Yes")
