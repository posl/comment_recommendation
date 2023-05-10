def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = 0
    for i in range(n):
        b += a[i] - (i+1)
    print(b)

if __name__ == '__main__':
    main()