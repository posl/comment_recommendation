def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_x = 0
    x = 0
    for i in range(n):
        x += a[i]
        if x > max_x:
            max_x = x
    print(max_x)

if __name__ == '__main__':
    main()