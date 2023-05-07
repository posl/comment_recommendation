def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))
    AB.sort()
    ans = 0
    prev = 0
    total = 0
    for i in range(len(AB)):
        if i > 0:
            ans += min(total, C) * (AB[i][0] - prev)
        prev = AB[i][0]
        total += AB[i][1]
    print(ans)

if __name__ == '__main__':
    main()