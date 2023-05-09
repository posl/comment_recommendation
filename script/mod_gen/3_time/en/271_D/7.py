def solve():
    N,S = map(int,input().split())
    cards = [list(map(int,input().split())) for i in range(N)]
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ''
            for j in range(N):
                if (i >> j) & 1:
                    ans += 'H'
                else:
                    ans += 'T'
            return 'Yes\n' + ans
    return 'No'

if __name__ == '__main__':
    solve()