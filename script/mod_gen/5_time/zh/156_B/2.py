def main():
    n, k = map(int, input().split())
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // k
    print(cnt)

if __name__ == '__main__':
    main()