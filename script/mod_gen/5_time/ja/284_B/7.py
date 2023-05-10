def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        cnt = 0
        for i in range(n):
            if a[i] % 2 == 1:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()