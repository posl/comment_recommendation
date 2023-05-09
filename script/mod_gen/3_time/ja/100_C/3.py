def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
    print(ans)

if __name__ == '__main__':
    main()