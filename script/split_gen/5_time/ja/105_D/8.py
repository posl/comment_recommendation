def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [0] + a
    for i in range(n):
        a[i+1] += a[i]
    a = [i%m for i in a]
    from collections import Counter
    c = Counter(a)
    ans = 0
    for i in c:
        ans += c[i]*(c[i]-1)//2
    print(ans)
