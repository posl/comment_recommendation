def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    n = 7 % k
    cnt = 1
    while n != 0:
        n = (n * 10 + 7) % k
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()