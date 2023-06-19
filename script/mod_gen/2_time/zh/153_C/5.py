def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if k >= n:
        print(0)
        return
    print(sum(h[:-k - 1]))

if __name__ == '__main__':
    main()