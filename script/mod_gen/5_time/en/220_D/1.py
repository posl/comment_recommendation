def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N - 1):
            a = A[j]
            b = A[j + 1]
            if (a + b) % 10 == i:
                A[j + 1] = (a + b) % 10
            else:
                A[j + 1] = (a * b) % 10
        ans[i] = A[N - 1]
        A = list(map(int, input().split()))
    print(*ans, sep="\n")

if __name__ == '__main__':
    solve()