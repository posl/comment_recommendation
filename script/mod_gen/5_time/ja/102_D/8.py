def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = 0
    for i in range(n):
        x += a[i]
        if x >= s/2:
            break
    y = x - a[i]
    print(min(abs(x-y), abs(s-x-(s-y))))

if __name__ == '__main__':
    main()