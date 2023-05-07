def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if A[i] == 2:
            if ans[i-1] == 1:
                ans[i] = 2
            else:
                ans[i] = 1
        else:
            if ans[i-1] == 0:
                ans[i] = 1
            else:
                ans[i] = 0
    print(*ans, sep='
')

if __name__ == '__main__':
    main()