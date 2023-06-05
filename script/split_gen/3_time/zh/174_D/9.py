def solve():
    N = int(input())
    c = input()
    w = c.count('W')
    ans = 0
    for i in range(w):
        if c[i] == 'R':
            ans += 1
    print(ans)
