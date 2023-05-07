def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(0, 4*n-1, 2):
        if a[i] != a[i+1]:
            print(a[i])
            break

if __name__ == '__main__':
    main()