def main():
    n,k = map(int,input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)
