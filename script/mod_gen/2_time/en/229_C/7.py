def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        a, b = map(int, input().split())
        cheese.append((a, b))
    cheese.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        ans += cheese[i][0] * min(cheese[i][1], w)
        w -= min(cheese[i][1], w)
    print(ans)

if __name__ == '__main__':
    main()