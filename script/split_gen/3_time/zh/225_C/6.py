def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**100):
        if B[0] == [(i-1)*7+j for j in range(1, 8)]:
            break
    for j in range(1, 10**100):
        if B[0][0] == (i-1)*7+j:
            break
    for k in range(N):
        for l in range(M):
            if B[k][l] != (i+k-1)*7+j+l:
                print("No")
                return
    print("Yes")
