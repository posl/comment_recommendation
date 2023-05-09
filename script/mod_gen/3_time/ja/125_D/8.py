def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    minus = 0
    min_minus = 10000000000
    for i in range(N):
        if A[i] < 0:
            minus += 1
        if abs(A[i]) < min_minus:
            min_minus = abs(A[i])
        ans += abs(A[i])
    if minus % 2 == 1:
        ans -= min_minus * 2
    print(ans)

if __name__ == '__main__':
    main()