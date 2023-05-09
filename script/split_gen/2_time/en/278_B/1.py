def main():
    h, m = map(int, input().split())
    while True:
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        if h % 10 == m // 10 and m % 10 == h // 10:
            print(h, m)
            break
        m += 1
main()
