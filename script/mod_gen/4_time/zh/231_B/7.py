def solve():
    N = int(input())
    d = {}
    for i in range(N):
        S = input()
        if S not in d:
            d[S] = 0
        d[S] += 1
    #print(d)
    print(max(d, key=d.get))
    return 0

if __name__ == '__main__':
    solve()