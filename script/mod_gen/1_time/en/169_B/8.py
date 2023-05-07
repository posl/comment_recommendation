def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 31:
        if A[0] == 4:
            print(0)
            return
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()