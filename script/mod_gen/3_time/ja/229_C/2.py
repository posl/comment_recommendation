def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        a, b = map(int, input().split())
        cheese.append((a, b))
    cheese.sort(key=lambda x: x[0] / x[1], reverse=True)
    ans = 0
    for a, b in cheese:
        ans += a * min(W // b, 1)
        W -= b * min(W // b, 1)
    print(ans)

if __name__ == '__main__':
    main()