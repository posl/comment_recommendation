def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print("draw")
            break
        if a > 0:
            taka += b
            a -= 1
        if taka >= x:
            print("taka")
            break
        if c > 0:
            taka += 0
            c -= 1
        if taka >= x:
            print("taka")
            break
        if d > 0:
            aoki += e
            d -= 1
        if aoki >= x:
            print("aoki")
            break
        if f > 0:
            aoki += 0
            f -= 1
        if aoki >= x:
            print("aoki")
            break

if __name__ == '__main__':
    main()