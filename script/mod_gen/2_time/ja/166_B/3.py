def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, N+1):
        for j in range(K):
            if i in A[j]:
                ans += 1
                break
    print(N-ans)

if __name__ == '__main__':
    main()