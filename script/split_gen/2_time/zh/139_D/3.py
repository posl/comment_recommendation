def main():
    n = int(input())
    h = list(map(int, input().split()))
    res = 0
    cnt = 0
    for i in range(n):
        if i == 0:
            res = h[i]
            cnt += 1
        else:
            if res <= h[i]:
                cnt += 1
                res = h[i]
    print(cnt)
