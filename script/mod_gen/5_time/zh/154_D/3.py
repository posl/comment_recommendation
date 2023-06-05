def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = sum(p[-k:])
    print(ans / 2)

if __name__ == '__main__':
    main()