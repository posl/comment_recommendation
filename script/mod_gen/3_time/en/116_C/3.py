def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while sum(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
        if r == 0:
            r = N - 1
        for i in range(l, r + 1):
            h[i] -= 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()