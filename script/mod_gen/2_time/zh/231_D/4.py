def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        print(n - (len(a) - bisect.bisect_left(a, x[i])))

if __name__ == '__main__':
    main()