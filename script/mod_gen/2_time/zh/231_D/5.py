def solve():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    AB.sort(key=lambda x:x[1])
    right = 0
    ans = 0
    for a,b in AB:
        if right < a:
            ans += 1
            right = b - 1
    print('Yes' if ans == 1 else 'No')

if __name__ == '__main__':
    solve()