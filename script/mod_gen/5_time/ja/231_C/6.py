def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        idx = bisect.bisect_left(a, x)
        print(n-idx)

if __name__ == '__main__':
    main()