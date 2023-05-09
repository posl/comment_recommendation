def solve():
    N = int(input())
    C = input()
    W = C.count('W')
    R = C.count('R')
    ans = min(W, R)
    w = 0
    r = 0
    for c in C:
        if c == 'W':
            w += 1
        else:
            r += 1
        ans = min(ans, max(w, r))
    print(ans)

if __name__ == '__main__':
    solve()