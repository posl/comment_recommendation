def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    
    ans = [0] * (10**9+2)
    for i in range(n):
        ans[a[i]] += 1
        ans[a[i]+b[i]] -= 1
    
    for i in range(1, 10**9+2):
        ans[i] += ans[i-1]
    
    for i in range(1, n+1):
        print(ans[i], end=' ')
