def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    x = 1
    y = 1
    cnt = 0
    while x * y < N:
        if x <= y:
            x += 1
        else:
            y += 1
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()