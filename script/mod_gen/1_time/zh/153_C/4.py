def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    total = sum(h)
    if k >= n:
        print(0)
    else:
        print(total - sum(h[-k-1:]))

if __name__ == '__main__':
    main()