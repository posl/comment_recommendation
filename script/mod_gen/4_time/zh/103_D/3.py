def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort(key=lambda x: x[1])
    ans = 0
    now = 0
    for a, b in ab:
        if a > now:
            now = b - 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()