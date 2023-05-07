def main():
    N = int(input())
    d = sorted(list(map(int, input().split())))
    print(d[N // 2] - d[N // 2 - 1])

if __name__ == '__main__':
    main()