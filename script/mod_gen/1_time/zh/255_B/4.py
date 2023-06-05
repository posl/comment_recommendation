def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    print(xy)
    print(a)
    print(n, k)

if __name__ == '__main__':
    main()