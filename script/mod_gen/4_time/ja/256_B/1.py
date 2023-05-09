def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p = p + a[i] - 1
    print(p)

if __name__ == '__main__':
    main()