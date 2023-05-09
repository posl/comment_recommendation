def solve(n, s, cards):
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return i
    return -1
n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]
result = solve(n, s, cards)

if __name__ == '__main__':
    solve()