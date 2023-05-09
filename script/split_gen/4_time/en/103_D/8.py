def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    a.sort(key=lambda x: x[1])
    cnt = 0
    bridge = 0
    for i in range(m):
        if a[i][0] > bridge:
            cnt += 1
            bridge = a[i][1] - 1
    print(cnt)
