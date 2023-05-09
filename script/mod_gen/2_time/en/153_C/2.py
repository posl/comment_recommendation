def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if n <= k:
        print(0)
    else:
        print(sum(h[:n-k]))

if __name__ == '__main__':
    main()