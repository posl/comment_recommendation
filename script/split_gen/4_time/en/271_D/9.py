def solve(n,s,card):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if ((i >> j) & 1):
                sum += card[j][0]
            else:
                sum += card[j][1]
        if sum == s:
            return i
    return -1
n,s = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]
ans = solve(n,s,card)
