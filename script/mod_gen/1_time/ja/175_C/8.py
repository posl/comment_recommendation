def main():
    x,k,d = map(int,input().split())
    if x < 0:
        x = -x
    if k <= x // d:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(abs((x % d) - d))

if __name__ == '__main__':
    main()