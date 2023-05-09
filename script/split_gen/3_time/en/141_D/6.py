def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(0)
    ans = 0
    for i in range(n):
        if a[i] <= a[i+1]:
            ans += a[i]
        else:
            ans += a[i]//2**(m)
            m -= 1
            if m == 0:
                break
    print(ans)
