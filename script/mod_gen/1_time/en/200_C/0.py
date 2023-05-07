def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for a in A:
        mod[a % 200] += 1
    ans = 0
    for m in mod:
        ans += m * (m - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()