def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            ans += 1
            continue
        break
    if A.count(A[0]) == N:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()