def main():
    L = int(input())
    N = 1
    M = 0
    while N*(N-1)//2 < L:
        N += 1
    print(N, N*(N-1)//2)
    for i in range(1, N):
        for j in range(i+1, N+1):
            print(i, j, min(L, i+j-2))
            M += 1
            L -= min(L, i+j-2)
            if L == 0:
                break
        if L == 0:
            break
    for i in range(M, N*(N-1)//2):
        print(1, 2, 0)
