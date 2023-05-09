def solve():
    N = int(input())
    towns = []
    for i in range(N):
        A, B = map(int, input().split())
        towns.append((A, B, A + B))
    towns.sort(key=lambda x: x[2], reverse=True)
    A_sum = sum([t[0] for t in towns])
    B_sum = 0
    ans = 0
    for i in range(N):
        A_sum -= towns[i][0]
        B_sum += towns[i][2]
        ans += 1
        if B_sum > A_sum:
            break
    print(ans)

if __name__ == '__main__':
    solve()