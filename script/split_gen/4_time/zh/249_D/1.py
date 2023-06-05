def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] == 0:
                cnt += d.get(a[i] // a[j], 0)
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    print(cnt)
