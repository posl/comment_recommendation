def solve():
    h = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                if a+b+c != h[0] or a+c+b != h[1] or a+b+c != h[2]:
                    continue
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            if d+e+f != w[0] or d+f+e != w[1] or d+e+f != w[2]:
                                continue
                            if a+d == b+e == c+f:
                                ans += 1
    print(ans)
solve()

if __name__ == '__main__':
    solve()