def main():
    x, y, r = map(float, input().split())
    x = int(x * 1000 + 0.5)
    y = int(y * 1000 + 0.5)
    r = int(r * 1000 + 0.5)
    #print(x, y, r)
    res = 0
    for a in range(x - r, x + r + 1):
        b = y + r
        while b >= y - r:
            if a * a + b * b <= r * r:
                break
            b -= 1
        res += b - y + 1
        #print(a, b, res)
    for a in range(x - r, x + r + 1):
        b = y - r
        while b <= y + r:
            if a * a + b * b <= r * r:
                break
            b += 1
        res += y - b + 1
        #print(a, b, res)
    print(res)

if __name__ == '__main__':
    main()