def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        res += i - bisect.bisect_left(a, a[i])
    print(res)

if __name__ == '__main__':
    main()