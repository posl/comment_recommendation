def solve():
    n,s = map(int,input().split())
    cards = [list(map(int,input().split())) for _ in range(n)]
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            ans = []
            for j in range(n):
                if i & (1<<j):
                    ans.append('T')
                else:
                    ans.append('H')
            print('Yes')
            print(''.join(ans))
            return
    print('No')
