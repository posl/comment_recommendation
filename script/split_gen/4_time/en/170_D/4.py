def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        ok = True
        for j in range(n):
            if i == j:
                continue
            if a[j] % a[i] == 0:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)
