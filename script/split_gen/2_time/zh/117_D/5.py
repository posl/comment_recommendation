def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    res = 0
    for i in range(40,-1,-1):
        s = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                s += 1
        if s <= n//2 and res + (1 << i) <= k:
            res += (1 << i)
    print(sum(a)^res)
