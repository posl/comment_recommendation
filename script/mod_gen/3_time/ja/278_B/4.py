def main():
    h, m = map(int, input().split())
    if m == 0:
        h += 1
        m = 0
    else:
        h += 1
        m = 60 - m
    print(h, m)

if __name__ == '__main__':
    main()