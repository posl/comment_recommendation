def main():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    print(sum(a[-k:]))

if __name__ == '__main__':
    main()