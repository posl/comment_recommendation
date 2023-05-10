def main():
    h, m = map(int, input().split())
    if m == 0:
        print(h, 0)
        return
    if m <= 12:
        print(h, m)
        return
    if h == 23:
        print(0, m - 12)
        return
    print(h + 1, m - 12)

if __name__ == '__main__':
    main()