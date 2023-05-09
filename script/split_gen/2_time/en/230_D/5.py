def main():
    n, d = map(int, input().split())
    l_r = []
    for _ in range(n):
        l, r = map(int, input().split())
        l_r.append([l, r])
    l_r.sort(key=lambda x: x[0])
    l = 0
    r = 0
    cnt = 0
    for i in range(n):
        if l_r[i][0] > r:
            l = l_r[i][0]
            r = l_r[i][0] + d - 1
            cnt += 1
        else:
            l = l_r[i][0]
            r = min(l_r[i][1], l_r[i][0] + d - 1)
    print(cnt)
