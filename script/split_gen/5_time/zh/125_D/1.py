def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
            a[i] *= -1
        ans += a[i]
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(a) * 2)
