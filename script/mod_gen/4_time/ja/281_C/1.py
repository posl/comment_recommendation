def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    T = T % total
    s = 0
    for i in range(N):
        if s <= T < s + A[i]:
            print(i + 1, T - s)
            break
        s += A[i]

if __name__ == '__main__':
    solve()