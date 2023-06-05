def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    while t > 0:
        for i in range(n):
            if t >= a[i]:
                t -= a[i]
            else:
                print(i+1, t)
                exit()
    print(1, 0)

if __name__ == '__main__':
    main()