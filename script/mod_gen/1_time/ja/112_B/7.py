def main():
    n, t = map(int, input().split())
    ans = 1001
    for i in range(n):
        c, tt = map(int, input().split())
        if tt <= t:
            ans = min(ans, c)
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

if __name__ == '__main__':
    main()