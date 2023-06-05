def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[-k:])
    print(s)

if __name__ == '__main__':
    main()