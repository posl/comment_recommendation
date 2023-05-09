def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    cur = 0
    ans = 0
    for a, b in ab:
        if cur < a:
            cur = b
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()