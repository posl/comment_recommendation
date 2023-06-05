def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0:
        print(a[0])
    else:
        for i in range(n):
            if a[i] % 2 == 0:
                print(a[i])
                break
            else:
                if i == n - 1:
                    print(-1)

if __name__ == '__main__':
    main()