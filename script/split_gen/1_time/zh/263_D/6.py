def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        if a[i] < 0:
            a[i] = -a[i]
            ans += l
        else:
            ans += r
    
    a.sort()
    
    if n % 2 == 1:
        ans -= 2 * min(a[0], a[n // 2])
    
    print(ans)
