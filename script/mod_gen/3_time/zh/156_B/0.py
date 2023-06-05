def main():
    n, k = map(int, input().split())
    cnt = 0
    while n > 0:
        n //= k
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()