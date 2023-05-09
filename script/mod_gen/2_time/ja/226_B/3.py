def main():
    N = int(input())
    D = {}
    for i in range(N):
        L, *A = map(int, input().split())
        if L not in D:
            D[L] = {}
        if tuple(A) not in D[L]:
            D[L][tuple(A)] = 0
        D[L][tuple(A)] += 1
    ans = 0
    for L in D:
        ans += len(D[L])
    print(ans)

if __name__ == '__main__':
    main()