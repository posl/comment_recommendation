def main():
    n,m = map(int,input().split())
    k = [0] * m
    s = [0] * m
    for i in range(m):
        k[i],*s[i] = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        light = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                for l in range(m):
                    if j+1 in s[l]:
                        light[l] += 1
        if all(light[l]%2 == p[l] for l in range(m)):
            ans += 1
    print(ans)
