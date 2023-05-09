def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            h[i+1] = h[i]
        ans = max(ans,h[i+1])
    print(ans)
