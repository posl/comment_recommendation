def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != A[N-1]:
        print(-1)
    else:
        ans = 0
        while A[0] % 2 == 0:
            A[0] = A[0] // 2
            ans += 1
        while A[0] % 3 == 0:
            A[0] = A[0] // 3
            ans += 1
        if A[0] == 1:
            print(ans)
        else:
            print(-1)

if __name__ == '__main__':
    main()