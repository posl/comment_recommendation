def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        a[i+1] = a[i+1] % a[i]
    print(a[-1])

if __name__ == '__main__':
    main()