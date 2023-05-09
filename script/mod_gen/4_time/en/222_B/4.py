def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        if a[i] < p:
            b += 1
    print(b)

if __name__ == '__main__':
    main()