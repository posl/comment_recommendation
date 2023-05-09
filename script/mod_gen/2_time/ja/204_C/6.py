def main():
    n, m = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(m)]
    print(n * (n - 1) - m)

if __name__ == '__main__':
    main()