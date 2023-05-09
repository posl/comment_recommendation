def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] == i:
            cnt += 1
    if cnt == n:
        print(n)
        exit(0)
    if cnt == n-1:
        print(n-1)
        exit(0)
    if cnt == n-2:
        print(n-2)
        exit(0)
    if cnt == n-3:
        print(n-3)
        exit(0)
    if cnt == n-4:
        print(n-4)
        exit(0)
    if cnt == n-5:
        print(n-5)
        exit(0)
    print(n-6)
    exit(0)

if __name__ == '__main__':
    main()