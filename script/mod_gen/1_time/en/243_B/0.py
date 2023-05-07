def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        if a[i] in b and a[i] != b[i]:
            d += 1
    print(c)
    print(d)

if __name__ == '__main__':
    main()