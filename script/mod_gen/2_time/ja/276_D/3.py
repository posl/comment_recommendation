def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] /= 2
            elif a[i] % 3 == 0:
                a[i] /= 3
            else:
                print(-1)
                return
        if len(set(a)) == 1:
            print(ans)
            return
        ans += 1

if __name__ == '__main__':
    main()