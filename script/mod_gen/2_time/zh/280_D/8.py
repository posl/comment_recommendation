def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        n = 1
        r = 1
        while True:
            r = (r * 10 + 1) % k
            n += 1
            if r == 0:
                break
        print(n)

if __name__ == '__main__':
    main()