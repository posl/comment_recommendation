def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x] - 1
            s += c[x]
            l += 1
            if x == i:
                break
            if l == k:
                break
        t = 0
        for j in range(l):
            x = p[x] - 1
            t += c[x]
            ans = max(ans,t + (k - j - 1) // l * s)
    print(ans)
main()
