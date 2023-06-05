def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0] * w / cheese[i][1]
            break
    print(int(ans))

if __name__ == '__main__':
    main()