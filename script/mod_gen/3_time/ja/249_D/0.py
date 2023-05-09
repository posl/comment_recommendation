def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                if A[i] // A[j] in d:
                    ans += d[A[i] // A[j]]
    print(ans)

if __name__ == '__main__':
    main()