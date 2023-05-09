def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                return ans
            else:
                A[i] = A[i] // 2
        ans += 1

if __name__ == '__main__':
    solve()