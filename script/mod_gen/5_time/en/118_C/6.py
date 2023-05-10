def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1,n):
        a[i] = a[i] % a[0]
    if a[0] == 1:
        print(1)
        return
    if a[0] == 0:
        print(0)
        return
    a[0] = a[0] % a[1]
    if a[1] == 1:
        print(1)
        return
    if a[1] == 0:
        print(0)
        return
    print(a[1])

if __name__ == '__main__':
    main()