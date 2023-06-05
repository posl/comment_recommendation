def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    print(a)
    print(xy)
    #print(n, k, a, xy)

if __name__ == '__main__':
    main()