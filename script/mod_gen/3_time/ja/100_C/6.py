def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 1:
                print(cnt)
                return
            else:
                a[i] /= 2
        cnt += 1

if __name__ == '__main__':
    main()