def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt2 = 0
    cnt3 = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt2 += 1
        while a[i] % 3 == 0:
            a[i] /= 3
            cnt3 += 1
    if len(set(a)) == 1:
        print(max(cnt2,cnt3) - min(cnt2,cnt3))
    else:
        print(-1)
