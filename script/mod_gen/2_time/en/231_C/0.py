def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_right(a, x[i]))

if __name__ == '__main__':
    main()