def main():
    N, M = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(M):
        l, r = map(int, input().split())
        L[l - 1] += 1
        R[r - 1] += 1
    res = 0
    for i in range(N):
        if i > 0:
            L[i] += L[i - 1]
        if L[i] == M:
            res += 1
        if R[i] > 0:
            L[i] -= R[i]
    print(res)

if __name__ == '__main__':
    main()