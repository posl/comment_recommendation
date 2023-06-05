def main():
    n, d = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for x, y in l:
        if x**2 + y**2 <= d**2:
            cnt += 1
    print(cnt)
main()
