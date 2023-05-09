def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all( a[i]%2 == 0 for i in range(n) ):
            a = [a[i]//2 for i in range(n)]
            count += 1
        else:
            break
    while True:
        if all( a[i]%3 == 0 for i in range(n) ):
            a = [a[i]//3 for i in range(n)]
            count += 1
        else:
            break
    if all( a[i] == a[0] for i in range(n) ):
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()