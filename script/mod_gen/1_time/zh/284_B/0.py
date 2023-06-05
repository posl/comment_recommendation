def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        a = list(map(int,input().split()))
        cnt = 0
        for j in range(m):
            if a[j] % 2 != 0:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()