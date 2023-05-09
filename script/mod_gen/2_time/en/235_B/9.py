def main():
    n = int(input())
    h = list(map(int, input().split()))
    maxh = 0
    for i in range(1, n):
        if h[i] >= h[i - 1]:
            maxh = max(maxh, h[i])
    print(maxh)

if __name__ == '__main__':
    main()