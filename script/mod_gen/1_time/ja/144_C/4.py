def main():
    N = int(input())
    x = 1
    y = 1
    cnt = 1
    while cnt < N:
        if x == y:
            x += 1
        else:
            y += 1
        cnt += 1
    print(x+y-1)

if __name__ == '__main__':
    main()