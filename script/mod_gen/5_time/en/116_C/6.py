def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            start = h.index(max(h))
            end = len(h) - h[::-1].index(max(h)) - 1
            ans += max(h)
            for i in range(start, end + 1):
                h[i] -= max(h)
    print(ans)

if __name__ == '__main__':
    main()