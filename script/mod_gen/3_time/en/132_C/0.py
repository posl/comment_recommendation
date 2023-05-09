def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N // 2] - d[N // 2 - 1])

if __name__ == '__main__':
    main()