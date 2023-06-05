def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        if sum([ans[j] for j in range(i, N, i)]) % 2 != a[i - 1]:
            ans.append(1)
        else:
            ans.append(0)
    M = sum(ans)
    print(M)
    if M > 0:
        print(*[i + 1 for i in range(N) if ans[i] == 1])
    return 0

if __name__ == '__main__':
    solve()