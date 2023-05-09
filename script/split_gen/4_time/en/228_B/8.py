def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    
    ans = 0
    for i in range(1, n+1):
        if x == i:
            continue
        if a[i] == x:
            ans += 1
            continue
        if a[a[i]] == x:
            ans += 1
            continue
    print(ans)
