def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n // 2]
    print(sum([abs(a[i] - (b + i)) for i in range(n)]))

if __name__ == '__main__':
    main()