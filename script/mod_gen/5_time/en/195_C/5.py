def main():
    N = int(input())
    cnt = 0
    i = 1
    while i <= N:
        cnt += N // i
        i *= 1000
    print(cnt)

if __name__ == '__main__':
    main()