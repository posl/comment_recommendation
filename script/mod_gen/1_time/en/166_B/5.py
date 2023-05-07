def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, N+1):
        for j in range(K):
            if i in A[j]:
                ans += 1
                break
    print(N - ans)

if __name__ == '__main__':
    main()