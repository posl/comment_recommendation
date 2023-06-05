def main():
    k = int(input())
    h = 21
    m = 0
    m += k
    while m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    print(str(h) + ':' + str(m))

if __name__ == '__main__':
    main()