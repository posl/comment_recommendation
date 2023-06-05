def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i - 1]:
            ok = True
            for j in range(i + 1, n):
                if a[j] % a[i] == 0:
                    ok = False
            if ok:
                ans += 1
    print(ans)
