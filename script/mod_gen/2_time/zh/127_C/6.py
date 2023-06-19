def main():
    n, m = map(int, input().split())
    l = 0
    r = n + 1
    for _ in range(m):
        l_i, r_i = map(int, input().split())
        l = max(l, l_i)
        r = min(r, r_i)
    print(max(0, r - l + 1))

if __name__ == '__main__':
    main()