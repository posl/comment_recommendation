def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[n-1] != a[n]:
        print(a[n-1])
    elif a[2*n-1] != a[2*n]:
        print(a[2*n-1])
    else:
        print(a[0])

if __name__ == '__main__':
    main()