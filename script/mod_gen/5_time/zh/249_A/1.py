def main():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    while x > 0:
        if t % (a + b + c) < a:
            x -= 1
        if x == 0:
            print('高桥')
            break
        if t % (d + e + f) < d:
            x -= 1
        if x == 0:
            print('青木')
            break
        t += 1
    else:
        print('画')

if __name__ == '__main__':
    main()