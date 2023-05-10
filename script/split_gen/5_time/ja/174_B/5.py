def main():
    n, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        if xy[i][0]**2 + xy[i][1]**2 <= d**2:
            cnt += 1
    print(cnt)
