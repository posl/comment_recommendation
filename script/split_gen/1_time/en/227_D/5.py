def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    #print(a)
    ans = 0
    for i in range(n):
        if i < k:
            continue
        ans += a[i]
    print(ans)
