def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for i in range(N):
        for j in range(N):
            if A[j] == 0:
                continue
            if A[i] % A[j] == 0:
                if A[i] // A[j] in d:
                    cnt += d[A[i] // A[j]]
    print(cnt)

if __name__ == '__main__':
    main()