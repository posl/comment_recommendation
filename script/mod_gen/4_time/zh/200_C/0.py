def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(i) for i in input().split()]
    cnt = [0] * 200
    for a in A:
        cnt[a % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()