def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [a[i] - i for i in range(n)]
    b.sort()
    c = [abs(b[i] - b[n // 2]) for i in range(n)]
    print(sum(c))

if __name__ == '__main__':
    main()