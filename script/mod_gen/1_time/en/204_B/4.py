def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if a[i] > 10:
            s += a[i] - 10
    print(s)

if __name__ == '__main__':
    main()