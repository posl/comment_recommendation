def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1 << n):
        cnt = 0
        num = 1
        for j in range(n):
            if i >> j & 1:
                cnt += 1
                num *= l[j][cnt]
        if cnt % 2 == 1:
            ans -= x // num
        else:
            ans += x // num
    print(ans)
