def main():
    a, b, c, d = map(int, input().split())
    if a > b * d:
        print(-1)
    else:
        count = 0
        while a > b * d:
            a += b
            a -= c
            count += 1
        print(count)

if __name__ == '__main__':
    main()