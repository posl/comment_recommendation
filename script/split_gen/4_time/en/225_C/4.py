def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    B = [B[i][j] for i in range(N) for j in range(M)]
    for i in range(10**5):
        A = [i*7+j+1 for j in range(7)]
        for j in range(1, 10**5):
            A += [A[-1]+7]
            if A[:M] == B or A[-M:] == B:
                print("Yes")
                return
    print("No")
    return
