def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 != 0:
                print(-1)
                return
            else:
                A[i] = A[i] // 2
        ans += 1
        if A.count(A[0]) == N:
            break
    print(ans - 1)

if __name__ == '__main__':
    main()