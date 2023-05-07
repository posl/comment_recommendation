def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if A[i] == cnt:
            ans[i] = ans[i-1] - 1
            cnt = 0
        else:
            ans[i] = ans[i-1] + 1
            cnt = A[i]
    print(*ans, sep='
')

if __name__ == '__main__':
    main()