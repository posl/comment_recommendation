def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    ans = 0
    if k >= n:
        print(ans)
    else:
        for i in range(k,n):
            ans += h[i]
        print(ans)
