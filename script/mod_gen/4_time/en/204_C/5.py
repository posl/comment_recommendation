def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()