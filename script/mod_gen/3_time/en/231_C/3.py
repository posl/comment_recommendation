def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        print(n - bisect.bisect_right(a, i - 1))

if __name__ == '__main__':
    main()