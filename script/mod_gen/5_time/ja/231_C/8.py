def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        ans = 0
        ans = n - bisect.bisect_left(a, x)
        print(ans)

if __name__ == '__main__':
    main()