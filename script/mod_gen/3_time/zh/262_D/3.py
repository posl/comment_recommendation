def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(1, 2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
        if s % 2 == 0:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    solve()