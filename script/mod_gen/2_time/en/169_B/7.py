def main():
    n = int(input())
    a = list(map(int, input().split()))
    z = 1
    for i in range(n):
        z *= a[i]
    if z > 10**18:
        print(-1)
    else:
        print(z)

if __name__ == '__main__':
    main()