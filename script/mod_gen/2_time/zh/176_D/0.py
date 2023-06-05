def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    b = []
    for i in range(n):
        b.append(a[i] - i)
    b = sorted(b)
    print(b[n // 2])

if __name__ == '__main__':
    main()