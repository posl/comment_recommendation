def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort(reverse=True)
    ans = sum(h)
    for i in range(k):
        ans -= h[i]
    print(ans)
