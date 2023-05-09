def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    B = [B[i][j] for i in range(N) for j in range(M)]
    for i in range(10**5):
        for j in range(7):
            if B == [i*7+j+k for k in range(N*M)]:
                print("Yes")
                return
    print("No")
