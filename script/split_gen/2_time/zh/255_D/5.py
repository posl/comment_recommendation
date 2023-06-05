def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        ans = 0
        while True:
            if x == a:
                print(ans)
                return
            if x < a:
                if (a - x) % d == 0:
                    print(ans + (a - x) // d)
                else:
                    print(ans + (a - x) // d + 1)
                return
            if n == 0:
                print(ans + x - a)
                return
            if x - a > d:
                ans += 1
                x -= 1
            else:
                ans += 1
                x += 1
            n -= 1
