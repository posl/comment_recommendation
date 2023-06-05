def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    print(p)
    print(n, k)
    print(p[0][0])

if __name__ == '__main__':
    main()