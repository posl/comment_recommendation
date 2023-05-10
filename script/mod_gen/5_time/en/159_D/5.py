def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] += 1
    ans = (N * (N - 1)) // 2
    for b in B[1:]:
        ans -= (b * (b - 1)) // 2
    for a in A:
        print(ans + B[a] - 1)

if __name__ == '__main__':
    solve()