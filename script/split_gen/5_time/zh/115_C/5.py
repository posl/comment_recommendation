def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(1, n-k+1):
        ans = min(ans, h[k-1+i]-h[i])
    print(ans)
main()
