def main():
    n, w = map(int, input().split())
    #print(n, w)
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    dp = [0 for i in range(w+1)]
    for i in range(n):
        for j in range(w, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]]+b[i])
    print(dp[w])
main()
