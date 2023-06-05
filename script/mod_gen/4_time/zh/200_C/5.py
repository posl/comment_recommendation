def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    cnt = [0] * 200
    for a in A:
        r = a % 200
        cnt[r] += 1
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()