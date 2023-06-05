def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()