def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
            else:
                print(cnt)
                exit()
        cnt += 1

if __name__ == '__main__':
    main()