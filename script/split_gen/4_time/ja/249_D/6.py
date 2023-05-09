def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*(n+1)
    for i in range(n):
        b[a[i]] += 1
    c = [0]*(n+1)
    for i in range(1,n+1):
        c[i] = c[i-1]+b[i]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]*a[j] > n:
                break
            else:
                ans += c[n//a[i]//a[j]]
    print(ans)
