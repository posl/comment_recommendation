def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = {}
    for i in range(n):
        if a[i] not in b:
            b[a[i]] = 1
        else:
            b[a[i]] += 1
    ans = 0
    for i in b:
        if b[i] % 2 == 1:
            ans += 1
    print(ans)
